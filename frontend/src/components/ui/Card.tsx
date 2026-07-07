import React from 'react';
import { motion, type HTMLMotionProps } from 'framer-motion';
import { cn } from '../../utils/cn';

interface CardProps extends HTMLMotionProps<'div'> {
  glass?: boolean;
}

export const Card = React.forwardRef<HTMLDivElement, CardProps>(
  ({ className, glass = true, ...props }, ref) => {
    return (
      <motion.div
        ref={ref}
        className={cn('rounded-xl p-6', glass ? 'glass' : 'bg-background-paper', className)}
        {...props}
      />
    );
  }
);
Card.displayName = 'Card';
