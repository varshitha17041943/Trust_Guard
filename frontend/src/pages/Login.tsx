import React, { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { useAuth } from '../contexts/AuthContext';
import api from '../utils/axios';
import { motion } from 'framer-motion';
import { ShieldCheck, Mail, Lock, ArrowRight, Loader2 } from 'lucide-react';

const Login = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);
  const { login } = useAuth();
  const navigate = useNavigate();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true); setError('');
    try {
      const res = await api.post('/auth/login', { email, password });
      login(res.data.access_token, res.data.user);
      navigate('/app');
    } catch (err: any) {
      setError(err.response?.data?.error || 'Failed to login');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-background flex items-center justify-center p-4">
      <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} className="glass-panel w-full max-w-md p-8">
        <div className="flex flex-col items-center mb-8">
          <ShieldCheck className="text-primary w-12 h-12 mb-4" />
          <h2 className="text-2xl font-bold">Welcome Back</h2>
          <p className="text-gray-400 text-sm mt-1">Sign in to TrustGuardAI</p>
        </div>
        
        {error && <div className="mb-6 p-3 bg-danger/10 border border-danger/30 text-danger text-sm rounded-lg text-center">{error}</div>}
        
        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <label className="block text-sm font-medium text-gray-300 mb-2">Email Address</label>
            <div className="relative">
              <Mail className="absolute left-3 top-1/2 -translate-y-1/2 text-gray-500 w-5 h-5" />
              <input type="email" required className="w-full bg-surface border border-border rounded-lg pl-10 pr-4 py-2.5 text-white focus:outline-none focus:border-primary" value={email} onChange={e => setEmail(e.target.value)} />
            </div>
          </div>
          <div>
            <div className="flex justify-between items-center mb-2">
              <label className="block text-sm font-medium text-gray-300">Password</label>
              <Link to="/forgot-password" className="text-xs text-primary hover:text-primary-dark transition">Forgot password?</Link>
            </div>
            <div className="relative">
              <Lock className="absolute left-3 top-1/2 -translate-y-1/2 text-gray-500 w-5 h-5" />
              <input type="password" required className="w-full bg-surface border border-border rounded-lg pl-10 pr-4 py-2.5 text-white focus:outline-none focus:border-primary" value={password} onChange={e => setPassword(e.target.value)} />
            </div>
          </div>
          <div className="flex items-center gap-2 mt-4">
            <input type="checkbox" id="remember" className="rounded border-gray-600 bg-surface text-primary focus:ring-primary" />
            <label htmlFor="remember" className="text-sm text-gray-400">Remember me for 7 days</label>
          </div>
          <button type="submit" disabled={loading} className="w-full btn-primary mt-6 flex justify-center items-center gap-2">
            {loading ? <Loader2 className="animate-spin" size={18} /> : <>Sign In <ArrowRight size={18} /></>}
          </button>
        </form>
        <p className="text-center mt-6 text-sm text-gray-400">
          Don't have an account? <Link to="/register" className="text-primary hover:text-primary-dark font-medium">Create one</Link>
        </p>
      </motion.div>
    </div>
  );
};

export default Login;
