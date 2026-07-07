import React from 'react';

const Footer = () => {
  return (
    <footer className="border-t border-white/10 bg-surface/30 mt-20 py-12 px-8">
      <div className="max-w-6xl mx-auto flex flex-col md:flex-row justify-between items-center gap-6">
        <div className="text-gray-400 text-sm">
          &copy; {new Date().getFullYear()} TrustGuardAI. All rights reserved.
        </div>
        <div className="flex gap-6 text-sm text-gray-400">
          <a href="#" className="hover:text-white transition">Privacy Policy</a>
          <a href="#" className="hover:text-white transition">Terms of Service</a>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
