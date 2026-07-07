import React from 'react';
import { motion } from 'framer-motion';
import { cn } from '../../utils/cn';

export const LoadingSpinner = ({ className }: { className?: string }) => (
  <motion.div
    animate={{ rotate: 360 }}
    transition={{ repeat: Infinity, duration: 1, ease: 'linear' }}
    className={cn('h-6 w-6 rounded-full border-2 border-primary border-t-transparent', className)}
  />
);
