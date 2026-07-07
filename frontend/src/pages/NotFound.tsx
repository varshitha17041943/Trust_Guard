import React from 'react';
import { Link } from 'react-router-dom';
import { motion } from 'framer-motion';
import { ShieldAlert } from 'lucide-react';

const NotFound = () => {
  return (
    <div className="min-h-screen bg-background flex flex-col items-center justify-center p-6 text-center">
      <motion.div
        initial={{ scale: 0.8, opacity: 0 }}
        animate={{ scale: 1, opacity: 1 }}
        transition={{ type: 'spring', bounce: 0.5 }}
      >
        <ShieldAlert size={100} className="text-primary/50 mx-auto mb-8" />
        <h1 className="text-7xl font-extrabold text-transparent bg-clip-text bg-gradient-to-br from-white to-gray-500 mb-4">
          404
        </h1>
        <h2 className="text-2xl font-bold mb-4">Page Not Found</h2>
        <p className="text-gray-400 max-w-md mx-auto mb-8">
          The page you are looking for has been moved, deleted, or possibly quarantined by our agents.
        </p>
        <Link to="/app" className="btn-primary">
          Return to Dashboard
        </Link>
      </motion.div>
    </div>
  );
};

export default NotFound;
