import React, { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { ChevronDown } from 'lucide-react';
import { cn } from '../../utils/cn';

interface AccordionItem {
  title: string;
  content: React.ReactNode;
}

export const Accordion = ({ items, className }: { items: AccordionItem[], className?: string }) => {
  const [openIndex, setOpenIndex] = useState<number | null>(null);

  return (
    <div className={cn('space-y-2', className)}>
      {items.map((item, i) => (
        <div key={i} className='border border-white/10 rounded-xl overflow-hidden bg-white/5'>
          <button
            onClick={() => setOpenIndex(openIndex === i ? null : i)}
            className='w-full flex items-center justify-between p-4 text-left hover:bg-white/5 transition-colors focus:outline-none'
          >
            <span className='font-medium'>{item.title}</span>
            <ChevronDown className={cn('h-5 w-5 text-text-muted transition-transform', openIndex === i && 'rotate-180')} />
          </button>
          <AnimatePresence>
            {openIndex === i && (
              <motion.div
                initial={{ height: 0, opacity: 0 }}
                animate={{ height: 'auto', opacity: 1 }}
                exit={{ height: 0, opacity: 0 }}
                transition={{ duration: 0.2 }}
              >
                <div className='p-4 pt-0 text-sm text-text-muted border-t border-white/10 mt-2'>
                  {item.content}
                </div>
              </motion.div>
            )}
          </AnimatePresence>
        </div>
      ))}
    </div>
  );
};
