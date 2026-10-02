export async function streamGenerate(payload:{topic:string;content_type?:string;tone?:string}, token:string, onDelta:(delta:string)=>void) {
  const response=await fetch(`${import.meta.env.VITE_API_URL ?? 'http://localhost:8000/api'}/ai/stream/`,{method:'POST',headers:{'Content-Type':'application/json',Authorization:`Bearer ${token}`},body:JSON.stringify(payload)});
  if(!response.ok || !response.body) throw new Error('stream failed');
  const reader=response.body.getReader(); const decoder=new TextDecoder();
  while(true){const {done,value}=await reader.read(); if(done) break; for(const line of decoder.decode(value,{stream:true}).split('\\n')){if(line.startsWith('data: ')){const data=line.slice(6); if(data==='[DONE]') return; try{const parsed=JSON.parse(data); if(parsed.delta) onDelta(parsed.delta);}catch{}}}}
}
