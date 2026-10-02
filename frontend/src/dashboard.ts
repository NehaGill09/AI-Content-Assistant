import { api } from './api';
export async function getUsage(){const {data}=await api.get('/ai/usage/'); return data as {requests:number;total_tokens:number;average_latency_ms:number;estimated_cost_usd:number};}
