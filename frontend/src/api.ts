import axios from 'axios';

export const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL ?? 'http://localhost:8000/api',
  timeout: 60000,
});

export async function generateContent(payload: { topic: string; content_type?: string; tone?: string }) {
  const { data } = await api.post('/ai/generate/', payload);
  return data;
}
