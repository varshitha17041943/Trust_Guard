import React from 'react';
import { Link } from 'react-router-dom';
import { ShieldCheck } from 'lucide-react';

const Navbar = () => {
  return (
    <nav className="fixed top-0 w-full z-50 glass-panel border-x-0 border-t-0 rounded-none h-20 flex items-center px-8 justify-between">
      <Link to="/" className="flex items-center gap-2 text-2xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-primary to-accent">
        <ShieldCheck className="w-8 h-8 text-primary" />
        TrustGuardAI
      </Link>
      <div className="hidden md:flex items-center gap-8 text-sm font-medium text-gray-300">
        <a href="#features" className="hover:text-white transition-colors">Features</a>
        <a href="#how-it-works" className="hover:text-white transition-colors">How It Works</a>
      </div>
      <div className="flex gap-4">
        <Link to="/app" className="btn-secondary hidden sm:block">Log In</Link>
        <Link to="/app" className="btn-primary">Get Started</Link>
      </div>
    </nav>
  );
};

export default Navbar;
