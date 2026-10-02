import React, { useState } from 'react';
import { createRoot } from 'react-dom/client';
import './styles.css';
import { generateContent } from './api';

type Result = { title: string; content: string; seo_keywords: string[] };

function App() {
  const [topic, setTopic] = useState('');
  const [tone, setTone] = useState('professional');
  const [type, setType] = useState('blog');
  const [out, setOut] = useState<Result | null>(null);
  const [error, setError] = useState('');
  const [busy, setBusy] = useState(false);

  async function generate() {
    setBusy(true); setError('');
    try { setOut(await generateContent({ topic, tone, content_type: type })); }
    catch { setError('Generation failed. Check your API configuration and authentication.'); }
    finally { setBusy(false); }
  }

  return <main>
    <span className="badge">AI CONTENT ASSISTANT</span>
    <h1>Ideas → publish-ready content.</h1>
    <p>Prompt-engineered generation with typed outputs, telemetry, throttling, Redis and Django.</p>
    <section>
      <textarea value={topic} onChange={e => setTopic(e.target.value)} placeholder="Describe what you want to create..." />
      <div className="controls">
        <select value={type} onChange={e => setType(e.target.value)}><option value="blog">Blog</option><option value="landing-page">Landing page</option><option value="social">Social post</option><option value="email">Email</option></select>
        <select value={tone} onChange={e => setTone(e.target.value)}><option>professional</option><option>friendly</option><option>bold</option><option>technical</option></select>
        <button onClick={generate} disabled={busy || !topic.trim()}>{busy ? 'Generating…' : 'Generate with AI →'}</button>
      </div>
      {error && <div role="alert">{error}</div>}
      {out && <article><h2>{out.title}</h2><p>{out.content}</p><small>{out.seo_keywords?.join(' • ')}</small></article>}
    </section>
  </main>;
}

createRoot(document.getElementById('root')!).render(<React.StrictMode><App /></React.StrictMode>);
