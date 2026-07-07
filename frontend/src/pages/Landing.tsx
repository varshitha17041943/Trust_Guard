import React from 'react';
import { Link } from 'react-router-dom';
import { motion } from 'framer-motion';
import { ShieldCheck, Zap, Lock, Globe, Cpu } from 'lucide-react';

const Landing = () => {
  return (
    <div className="flex flex-col items-center">
      {/* Hero Section */}
      <section className="w-full max-w-6xl mx-auto px-6 py-32 flex flex-col items-center text-center">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.7 }}
        >
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-primary/10 border border-primary/20 text-primary text-sm font-medium mb-8">
            <Zap size={14} /> 
            Google ADK Multi-Agent Architecture
          </div>
          <h1 className="text-5xl md:text-7xl font-extrabold tracking-tight mb-8 leading-tight">
            Protect Your Digital Life with <br />
            <span className="bg-clip-text text-transparent bg-gradient-to-r from-primary via-accent to-primary animate-gradient-x">
              Explainable AI
            </span>
          </h1>
          <p className="text-xl text-gray-400 max-w-2xl mx-auto mb-12">
            Detect fake websites and malicious QR codes before you log in or pay. TrustGuardAI uses a swarm of autonomous agents to interrogate threats in real-time.
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <Link to="/app" className="btn-primary text-lg px-8 py-4">
              Launch Dashboard
            </Link>
            <Link to="/app/scanner" className="btn-secondary text-lg px-8 py-4">
              Scan a URL Now
            </Link>
          </div>
        </motion.div>
      </section>

      {/* Features Section */}
      <section id="features" className="w-full max-w-6xl mx-auto px-6 py-20">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          {[
            { icon: Globe, title: "Deep URL Analysis", desc: "WHOIS anomaly detection, SSL interrogation, and typosquatting prevention." },
            { icon: Cpu, title: "Antigravity Engine", desc: "DAG-based concurrent agent execution cuts scan times by 75%." },
            { icon: Lock, title: "MCP Threat Intel", desc: "Isolated execution of cybersecurity tools preventing direct LLM network access." }
          ].map((feature, idx) => (
            <motion.div 
              key={idx}
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ delay: idx * 0.2 }}
              className="glass-panel p-8"
            >
              <div className="w-12 h-12 rounded-xl bg-primary/20 flex items-center justify-center mb-6">
                <feature.icon className="text-primary w-6 h-6" />
              </div>
              <h3 className="text-xl font-bold mb-3">{feature.title}</h3>
              <p className="text-gray-400 leading-relaxed">{feature.desc}</p>
            </motion.div>
          ))}
        </div>
      </section>

      {/* Stats */}
      <section className="w-full border-y border-white/10 bg-surface/50 py-20 mt-10">
        <div className="max-w-6xl mx-auto px-6 grid grid-cols-2 md:grid-cols-4 gap-8 text-center">
          {[ { v: "99.9%", l: "Detection Rate" }, { v: "< 2s", l: "Scan Speed" }, { v: "5+", l: "Parallel Agents" }, { v: "0", l: "False Positives" } ].map((stat, idx) => (
            <div key={idx} className="space-y-2">
              <div className="text-4xl font-extrabold bg-clip-text text-transparent bg-gradient-to-br from-white to-gray-400">
                {stat.v}
              </div>
              <div className="text-sm text-gray-500 uppercase tracking-widest font-semibold">{stat.l}</div>
            </div>
          ))}
        </div>
      </section>
    </div>
  );
};

export default Landing;
