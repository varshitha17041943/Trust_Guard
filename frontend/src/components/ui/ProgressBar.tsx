import React from 'react';
import { motion } from 'framer-motion';
import { cn } from '../../utils/cn';

export const ProgressBar = ({ progress, className }: { progress: number; className?: string }) => (
  <div className={cn('h-2 w-full overflow-hidden rounded-full bg-white/10', className)}>
    <motion.div
      initial={{ width: 0 }}
      animate={{ width: `${progress}%` }}
      transition={{ duration: 0.5 }}
      className='h-full bg-primary'
    />
  </div>
);
