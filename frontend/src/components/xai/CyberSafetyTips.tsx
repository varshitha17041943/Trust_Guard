import React, { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { Lightbulb } from 'lucide-react';

const tips = [
  "Always verify website URLs before logging in.",
  "Avoid clicking links from unknown or unsolicited emails.",
  "Never share One-Time Passwords (OTPs) with anyone.",
  "Use a reliable password manager to generate and store unique passwords.",
  "Enable Multi-Factor Authentication (MFA) whenever possible.",
  "Check for 'https://' but remember scammers can use it too.",
  "Beware of urgent messages demanding immediate action.",
  "Keep your browser and operating system up to date.",
  "Public Wi-Fi is insecure; use a VPN when accessing sensitive accounts.",
  "If a deal looks too good to be true, it probably is a scam."
];

export const CyberSafetyTips = () => {
  const [index, setIndex] = useState(0);

  useEffect(() => {
    const timer = setInterval(() => {
      setIndex(prev => (prev + 1) % tips.length);
    }, 6000);
    return () => clearInterval(timer);
  }, []);

  return (
    <div className="bg-white/5 border border-white/10 rounded-xl p-4 flex items-center gap-4">
      <div className="bg-yellow-500/20 p-2 rounded-full shrink-0">
        <Lightbulb className="w-5 h-5 text-yellow-500" />
      </div>
      <div className="flex-grow overflow-hidden relative h-6">
        <AnimatePresence mode="wait">
          <motion.p
            key={index}
            initial={{ opacity: 0, y: 10 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -10 }}
            className="text-sm font-medium text-white/90 absolute inset-0"
          >
            {tips[index]}
          </motion.p>
        </AnimatePresence>
      </div>
    </div>
  );
};
