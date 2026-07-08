---
name: HCS Premium UI Designer
description: HCS Premium UI/UX design skill for Next.js/React projects. Transforms any website into ultra-premium experience with glassmorphism, scroll animations, micro-interactions, and consistent color theming. Uses Framer Motion for animations, Tailwind CSS for styling, and follows WCAG accessibility standards.
license: MIT
compatibility: opencode
categories: [ui-design, ux, animations, transitions, glassmorphism, premium-design, accessibility]
metadata:
  author: HCS
  version: "1.0"
  last_updated: "2026-07-04"
  scope: universal
---

# ═══════════════════════════════════════════════════════════════════════
# HCS PREMIUM UI DESIGNER SKILL v1.0
# Ultra-Premium Website Enhancement System
# ═══════════════════════════════════════════════════════════════════════

> **"Transform any website into an ultra-premium experience with consistent theming, fluid animations, and delightful micro-interactions."**

---

## TABLE OF CONTENTS

1. [Design Philosophy](#1-design-philosophy)
2. [Color Theme System](#2-color-theme-system)
3. [Animation Framework](#3-animation-framework)
4. [Glass Morphism System](#4-glass-morphism-system)
5. [Micro-Interactions](#5-micro-interactions)
6. [Scroll Animations](#6-scroll-animations)
7. [Transition Patterns](#7-transition-patterns)
8. [Component Patterns](#8-component-patterns)
9. [Typography System](#9-typography-system)
10. [Spacing & Layout](#10-spacing--layout)
11. [Accessibility](#11-accessibility)
12. [Implementation Guide](#12-implementation-guide)

---

## 1. Design Philosophy

### Core Principles
- **Consistency**: Every component follows the same color theme and animation patterns
- **Delight**: Micro-interactions that make users smile
- **Performance**: Animations run at 60fps using GPU-accelerated properties
- **Accessibility**: All animations respect `prefers-reduced-motion`
- **Progressive Enhancement**: Works without JS, enhanced with JS

### Design Tokens
```typescript
const designTokens = {
  colors: {
    primary: "emerald",    // Main accent
    secondary: "cyan",     // Secondary accent
    tertiary: "purple",    // Tertiary accent
    background: "slate",   // Background shades
    surface: "white",      // Card surfaces
  },
  animations: {
    duration: {
      fast: 0.15,
      normal: 0.3,
      slow: 0.5,
      slower: 0.8,
    },
    easing: {
      easeOut: [0.16, 1, 0.3, 1],
      easeInOut: [0.65, 0, 0.35, 1],
      spring: { type: "spring", stiffness: 300, damping: 30 },
    },
  },
  glass: {
    blur: "blur(12px)",
    opacity: "bg-white/[0.03]",
    border: "border-white/[0.06]",
  },
};
```

---

## 2. Color Theme System

### Hankith Numerology Theme
```css
:root {
  /* Primary - Emerald */
  --color-primary-50: rgb(16, 185, 129, 0.05);
  --color-primary-100: rgb(16, 185, 129, 0.1);
  --color-primary-200: rgb(16, 185, 129, 0.2);
  --color-primary-300: rgb(52, 211, 153);
  --color-primary-400: rgb(16, 185, 129);
  --color-primary-500: rgb(5, 150, 105);
  
  /* Secondary - Cyan */
  --color-secondary-50: rgb(6, 182, 212, 0.05);
  --color-secondary-100: rgb(6, 182, 212, 0.1);
  --color-secondary-200: rgb(6, 182, 212, 0.2);
  --color-secondary-300: rgb(34, 211, 238);
  --color-secondary-400: rgb(6, 182, 212);
  
  /* Tertiary - Purple */
  --color-tertiary-50: rgb(139, 92, 246, 0.05);
  --color-tertiary-100: rgb(139, 92, 246, 0.1);
  --color-tertiary-200: rgb(139, 92, 246, 0.2);
  --color-tertiary-300: rgb(167, 139, 250);
  --color-tertiary-400: rgb(139, 92, 246);
  
  /* Background - Slate */
  --color-bg-950: rgb(2, 6, 23);
  --color-bg-900: rgb(15, 23, 42);
  --color-bg-800: rgb(30, 41, 59);
  
  /* Semantic */
  --color-success: rgb(34, 197, 94);
  --color-warning: rgb(251, 191, 36);
  --color-error: rgb(239, 68, 68);
  --color-info: rgb(59, 130, 246);
}
```

### Gradient Presets
```typescript
const gradients = {
  // Card backgrounds
  cardPrimary: "bg-gradient-to-br from-emerald-500/[0.03] to-cyan-500/[0.03]",
  cardSecondary: "bg-gradient-to-br from-purple-500/[0.03] to-pink-500/[0.03]",
  cardWarm: "bg-gradient-to-br from-amber-500/[0.03] to-orange-500/[0.03]",
  
  // Button gradients
  btnPrimary: "bg-gradient-to-r from-emerald-600 to-cyan-600",
  btnSecondary: "bg-gradient-to-r from-purple-600 to-pink-600",
  btnWarm: "bg-gradient-to-r from-amber-600 to-orange-600",
  
  // Hero backgrounds
  heroDark: "bg-gradient-to-b from-slate-950 via-slate-900 to-slate-950",
  heroRadial: "bg-[radial-gradient(ellipse_at_top,_var(--tw-gradient-stops))]",
  
  // Text gradients
  textGradientPrimary: "bg-gradient-to-r from-emerald-300 to-cyan-300 bg-clip-text text-transparent",
  textGradientSecondary: "bg-gradient-to-r from-purple-300 to-pink-300 bg-clip-text text-transparent",
};
```

---

## 3. Animation Framework

### Framer Motion Presets
```typescript
// Container animations
export const containerVariants = {
  hidden: { opacity: 0 },
  visible: {
    opacity: 1,
    transition: { staggerChildren: 0.1, delayChildren: 0.1 },
  },
};

// Item animations
export const itemVariants = {
  hidden: { opacity: 0, y: 20 },
  visible: {
    opacity: 1,
    y: 0,
    transition: { type: "spring", stiffness: 300, damping: 30 },
  },
};

// Card hover
export const cardHoverVariants = {
  rest: { scale: 1, y: 0 },
  hover: { 
    scale: 1.02, 
    y: -4,
    transition: { type: "spring", stiffness: 400, damping: 25 },
  },
};

// Fade in directions
export const fadeInUp = {
  hidden: { opacity: 0, y: 30 },
  visible: { opacity: 1, y: 0, transition: { duration: 0.5, ease: [0.16, 1, 0.3, 1] } },
};

export const fadeInLeft = {
  hidden: { opacity: 0, x: -30 },
  visible: { opacity: 1, x: 0, transition: { duration: 0.5, ease: [0.16, 1, 0.3, 1] } },
};

export const fadeInRight = {
  hidden: { opacity: 0, x: 30 },
  visible: { opacity: 1, x: 0, transition: { duration: 0.5, ease: [0.16, 1, 0.3, 1] } },
};

export const fadeInScale = {
  hidden: { opacity: 0, scale: 0.9 },
  visible: { opacity: 1, scale: 1, transition: { duration: 0.5, ease: [0.16, 1, 0.3, 1] } },
};

// Page transitions
export const pageTransition = {
  initial: { opacity: 0, y: 20 },
  animate: { opacity: 1, y: 0, transition: { duration: 0.4, ease: [0.16, 1, 0.3, 1] } },
  exit: { opacity: 0, y: -20, transition: { duration: 0.2 } },
};

// Stagger children
export const staggerContainer = {
  hidden: { opacity: 0 },
  visible: {
    opacity: 1,
    transition: { staggerChildren: 0.08, delayChildren: 0.1 },
  },
};

export const staggerItem = {
  hidden: { opacity: 0, y: 15 },
  visible: {
    opacity: 1,
    y: 0,
    transition: { type: "spring", stiffness: 300, damping: 30 },
  },
};
```

### CSS Animation Classes
```css
/* Smooth reveal */
@keyframes reveal {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}
.animate-reveal { animation: reveal 0.6s ease-out forwards; }

/* Glow pulse */
@keyframes glow-pulse {
  0%, 100% { box-shadow: 0 0 20px rgba(16, 185, 129, 0.2); }
  50% { box-shadow: 0 0 40px rgba(16, 185, 129, 0.4); }
}
.animate-glow { animation: glow-pulse 2s ease-in-out infinite; }

/* Float */
@keyframes float {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-10px); }
}
.animate-float { animation: float 3s ease-in-out infinite; }

/* Shimmer */
@keyframes shimmer {
  0% { background-position: -200% 0; }
  100% { background-position: 200% 0; }
}
.animate-shimmer {
  background: linear-gradient(90deg, transparent, rgba(255,255,255,0.1), transparent);
  background-size: 200% 100%;
  animation: shimmer 2s infinite;
}

/* Spin slow */
@keyframes spin-slow { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }
.animate-spin-slow { animation: spin-slow 8s linear infinite; }
```

---

## 4. Glass Morphism System

### Glass Card Component
```tsx
interface GlassCardProps {
  children: React.ReactNode;
  variant?: "default" | "primary" | "secondary" | "warm";
  hover?: boolean;
  className?: string;
}

export function GlassCard({ children, variant = "default", hover = true, className }: GlassCardProps) {
  const variants = {
    default: "bg-white/[0.03] border-white/[0.06]",
    primary: "bg-emerald-500/[0.03] border-emerald-500/10",
    secondary: "bg-purple-500/[0.03] border-purple-500/10",
    warm: "bg-amber-500/[0.03] border-amber-500/10",
  };

  return (
    <motion.div
      whileHover={hover ? { y: -2, scale: 1.01 } : undefined}
      transition={{ type: "spring", stiffness: 400, damping: 25 }}
      className={`
        rounded-2xl border backdrop-blur-xl
        ${variants[variant]}
        ${className}
      `}
    >
      {children}
    </motion.div>
  );
}
```

### Glass Effect Classes
```css
/* Base glass */
.glass {
  background: rgba(255, 255, 255, 0.03);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border: 1px solid rgba(255, 255, 255, 0.06);
}

/* Glass with gradient */
.glass-gradient {
  background: linear-gradient(
    135deg,
    rgba(255, 255, 255, 0.05) 0%,
    rgba(255, 255, 255, 0.02) 100%
  );
  backdrop-filter: blur(12px);
  border: 1px solid rgba(255, 255, 255, 0.08);
}

/* Glass hover effect */
.glass-hover {
  transition: all 0.3s ease;
}
.glass-hover:hover {
  background: rgba(255, 255, 255, 0.06);
  border-color: rgba(255, 255, 255, 0.1);
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
}
```

---

## 5. Micro-Interactions

### Button Interactions
```tsx
// Magnetic button effect
export function MagneticButton({ children, className }: { children: React.ReactNode; className?: string }) {
  const [position, setPosition] = useState({ x: 0, y: 0 });

  const handleMouse = (e: React.MouseEvent) => {
    const { clientX, clientY } = e;
    const { left, top, width, height } = e.currentTarget.getBoundingClientRect();
    const x = (clientX - left - width / 2) * 0.15;
    const y = (clientY - top - height / 2) * 0.15;
    setPosition({ x, y });
  };

  return (
    <motion.button
      onMouseMove={handleMouse}
      onMouseLeave={() => setPosition({ x: 0, y: 0 })}
      animate={{ x: position.x, y: position.y }}
      transition={{ type: "spring", stiffness: 150, damping: 15 }}
      className={className}
    >
      {children}
    </motion.button>
  );
}

// Ripple effect
export function RippleButton({ children, onClick, className }: { children: React.ReactNode; onClick?: () => void; className?: string }) {
  const [ripples, setRipples] = useState<{ x: number; y: number; id: number }[]>([]);

  const addRipple = (e: React.MouseEvent) => {
    const rect = e.currentTarget.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;
    const id = Date.now();
    setRipples([...ripples, { x, y, id }]);
    setTimeout(() => setRipples(ripples.filter((r) => r.id !== id)), 600);
    onClick?.();
  };

  return (
    <button onClick={addRipple} className={`relative overflow-hidden ${className}`}>
      {ripples.map((ripple) => (
        <span
          key={ripple.id}
          className="absolute rounded-full bg-white/30 animate-ping"
          style={{ left: ripple.x, top: ripple.y, transform: "translate(-50%, -50%)" }}
        />
      ))}
      {children}
    </button>
  );
}
```

### Input Interactions
```tsx
// Floating label input
export function FloatingInput({ label, type = "text", value, onChange }: { label: string; type?: string; value: string; onChange: (v: string) => void }) {
  const [focused, setFocused] = useState(false);
  const hasValue = value.length > 0;

  return (
    <div className="relative">
      <input
        type={type}
        value={value}
        onChange={(e) => onChange(e.target.value)}
        onFocus={() => setFocused(true)}
        onBlur={() => setFocused(false)}
        className="w-full px-4 pt-6 pb-2 rounded-xl bg-white/[0.04] border border-white/[0.08] text-white text-sm focus:outline-none focus:border-emerald-500/40 transition-colors peer"
        placeholder=" "
      />
      <label className={`absolute left-4 transition-all duration-200 pointer-events-none ${
        focused || hasValue ? "top-2 text-[10px] text-emerald-400/60" : "top-1/2 -translate-y-1/2 text-sm text-white/30"
      }`}>
        {label}
      </label>
    </div>
  );
}
```

### Card Interactions
```tsx
// Tilt card effect
export function TiltCard({ children, className }: { children: React.ReactNode; className?: string }) {
  const [tilt, setTilt] = useState({ x: 0, y: 0 });

  const handleMouse = (e: React.MouseEvent) => {
    const { clientX, clientY } = e;
    const { left, top, width, height } = e.currentTarget.getBoundingClientRect();
    const x = ((clientY - top) / height - 0.5) * 10;
    const y = ((clientX - left) / width - 0.5) * -10;
    setTilt({ x, y });
  };

  return (
    <motion.div
      onMouseMove={handleMouse}
      onMouseLeave={() => setTilt({ x: 0, y: 0 })}
      animate={{ rotateX: tilt.x, rotateY: tilt.y }}
      transition={{ type: "spring", stiffness: 300, damping: 30 }}
      style={{ perspective: 1000 }}
      className={className}
    >
      {children}
    </motion.div>
  );
}
```

---

## 6. Scroll Animations

### Intersection Observer Hook
```tsx
export function useScrollReveal(threshold = 0.1) {
  const ref = useRef<HTMLDivElement>(null);
  const [isVisible, setIsVisible] = useState(false);

  useEffect(() => {
    const observer = new IntersectionObserver(
      ([entry]) => {
        if (entry.isIntersecting) {
          setIsVisible(true);
          observer.unobserve(entry.target);
        }
      },
      { threshold }
    );

    if (ref.current) observer.observe(ref.current);
    return () => observer.disconnect();
  }, [threshold]);

  return { ref, isVisible };
}

// Usage
export function ScrollRevealSection({ children }: { children: React.ReactNode }) {
  const { ref, isVisible } = useScrollReveal(0.2);

  return (
    <motion.div
      ref={ref}
      initial={{ opacity: 0, y: 30 }}
      animate={isVisible ? { opacity: 1, y: 0 } : {}}
      transition={{ duration: 0.6, ease: [0.16, 1, 0.3, 1] }}
    >
      {children}
    </motion.div>
  );
}
```

### Parallax Effect
```tsx
export function ParallaxSection({ children, speed = 0.5 }: { children: React.ReactNode; speed?: number }) {
  const [offset, setOffset] = useState(0);

  useEffect(() => {
    const handleScroll = () => {
      setOffset(window.scrollY * speed);
    };
    window.addEventListener("scroll", handleScroll, { passive: true });
    return () => window.removeEventListener("scroll", handleScroll);
  }, [speed]);

  return (
    <div style={{ transform: `translateY(${offset}px)` }}>
      {children}
    </div>
  );
}
```

---

## 7. Transition Patterns

### Page Transitions (Next.js App Router)
```tsx
"use client";

import { motion, AnimatePresence } from "framer-motion";
import { usePathname } from "next/navigation";

export function PageTransition({ children }: { children: React.ReactNode }) {
  const pathname = usePathname();

  return (
    <AnimatePresence mode="wait">
      <motion.div
        key={pathname}
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        exit={{ opacity: 0, y: -20 }}
        transition={{ duration: 0.3, ease: [0.16, 1, 0.3, 1] }}
      >
        {children}
      </motion.div>
    </AnimatePresence>
  );
}
```

### Modal Transitions
```tsx
export function ModalTransition({ isOpen, onClose, children }: { isOpen: boolean; onClose: () => void; children: React.ReactNode }) {
  return (
    <AnimatePresence>
      {isOpen && (
        <>
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            className="fixed inset-0 bg-black/60 backdrop-blur-sm z-50"
            onClick={onClose}
          />
          <motion.div
            initial={{ opacity: 0, scale: 0.95, y: 20 }}
            animate={{ opacity: 1, scale: 1, y: 0 }}
            exit={{ opacity: 0, scale: 0.95, y: 20 }}
            transition={{ type: "spring", stiffness: 300, damping: 30 }}
            className="fixed inset-0 z-50 flex items-center justify-center p-4"
          >
            {children}
          </motion.div>
        </>
      )}
    </AnimatePresence>
  );
}
```

### List Animations
```tsx
export function AnimatedList({ items }: { items: string[] }) {
  return (
    <motion.ul
      variants={containerVariants}
      initial="hidden"
      animate="visible"
    >
      {items.map((item, i) => (
        <motion.li key={i} variants={itemVariants}>
          {item}
        </motion.li>
      ))}
    </motion.ul>
  );
}
```

---

## 8. Component Patterns

### Premium Score Ring
```tsx
export function PremiumScoreRing({ score, size = 80, strokeWidth = 6 }: { score: number; size?: number; strokeWidth?: number }) {
  const radius = (size - strokeWidth) / 2;
  const circumference = 2 * Math.PI * radius;
  const color = score >= 70 ? "#34d399" : score >= 50 ? "#fbbf24" : "#f87171";

  return (
    <div className="relative inline-flex items-center justify-center">
      <svg width={size} height={size} viewBox={`0 0 ${size} ${size}`}>
        <circle cx={size / 2} cy={size / 2} r={radius} fill="none" stroke="rgba(255,255,255,0.05)" strokeWidth={strokeWidth} />
        <motion.circle
          cx={size / 2} cy={size / 2} r={radius}
          fill="none" stroke={color} strokeWidth={strokeWidth}
          strokeDasharray={circumference}
          strokeDashoffset={circumference}
          strokeLinecap="round"
          transform={`rotate(-90 ${size / 2} ${size / 2})`}
          animate={{ strokeDashoffset: circumference - (score / 100) * circumference }}
          transition={{ duration: 1.5, ease: [0.16, 1, 0.3, 1], delay: 0.3 }}
          style={{ filter: `drop-shadow(0 0 8px ${color}60)` }}
        />
      </svg>
      <div className="absolute inset-0 flex flex-col items-center justify-center">
        <motion.span
          initial={{ opacity: 0, scale: 0.5 }}
          animate={{ opacity: 1, scale: 1 }}
          transition={{ delay: 0.5, type: "spring", stiffness: 300, damping: 20 }}
          className="text-2xl font-bold"
          style={{ color }}
        >
          {score}
        </motion.span>
        <span className="text-[9px] text-white/25">/ 100</span>
      </div>
    </div>
  );
}
```

### Premium Stat Card
```tsx
export function PremiumStatCard({ label, value, icon: Icon, color = "emerald" }: { label: string; value: string | number; icon: React.ElementType; color?: string }) {
  return (
    <motion.div
      whileHover={{ y: -2, scale: 1.02 }}
      transition={{ type: "spring", stiffness: 400, damping: 25 }}
      className={`rounded-2xl border border-${color}-500/15 bg-${color}-500/[0.03] p-4 text-center`}
    >
      <div className={`w-10 h-10 rounded-xl bg-${color}-500/15 flex items-center justify-center mx-auto mb-3`}>
        <Icon className={`w-5 h-5 text-${color}-400`} />
      </div>
      <p className="text-2xl font-bold text-white/90">{value}</p>
      <p className="text-[10px] text-white/30 uppercase tracking-wider mt-1">{label}</p>
    </motion.div>
  );
}
```

### Premium Section Header
```tsx
export function PremiumSectionHeader({ icon: Icon, title, subtitle, color = "amber" }: { icon: React.ElementType; title: string; subtitle?: string; color?: string }) {
  return (
    <motion.div
      initial={{ opacity: 0, x: -20 }}
      whileInView={{ opacity: 1, x: 0 }}
      viewport={{ once: true }}
      transition={{ duration: 0.5, ease: [0.16, 1, 0.3, 1] }}
      className="flex items-center gap-3 mb-6"
    >
      <div className={`w-10 h-10 rounded-xl bg-gradient-to-br from-${color}-500/20 to-${color}-600/20 border border-${color}-500/20 flex items-center justify-center`}>
        <Icon className={`w-5 h-5 text-${color}-400`} />
      </div>
      <div>
        <h2 className="text-lg font-bold text-white/90">{title}</h2>
        {subtitle && <p className="text-xs text-white/40 mt-0.5">{subtitle}</p>}
      </div>
    </motion.div>
  );
}
```

---

## 9. Typography System

### Font Classes
```css
/* Headings */
.heading-xl { @apply text-3xl sm:text-4xl font-extrabold tracking-tight; }
.heading-lg { @apply text-2xl sm:text-3xl font-extrabold; }
.heading-md { @apply text-xl sm:text-2xl font-bold; }
.heading-sm { @apply text-lg font-bold; }

/* Body */
.body-lg { @apply text-base leading-relaxed; }
.body-md { @apply text-sm leading-relaxed; }
.body-sm { @apply text-xs leading-relaxed; }
.body-xs { @apply text-[11px] leading-relaxed; }

/* Labels */
.label-lg { @apply text-xs font-bold uppercase tracking-wider; }
.label-md { @apply text-[10px] font-bold uppercase tracking-wider; }
.label-sm { @apply text-[9px] font-bold uppercase tracking-wider; }

/* Gradient text */
.text-gradient-primary {
  @apply bg-gradient-to-r from-emerald-300 to-cyan-300 bg-clip-text text-transparent;
}
.text-gradient-secondary {
  @apply bg-gradient-to-r from-purple-300 to-pink-300 bg-clip-text text-transparent;
}
.text-gradient-warm {
  @apply bg-gradient-to-r from-amber-300 to-orange-300 bg-clip-text text-transparent;
}
```

---

## 10. Spacing & Layout

### Consistent Spacing
```css
/* Section spacing */
.section-spacing { @apply py-12 sm:py-16 lg:py-20; }

/* Card padding */
.card-padding { @apply p-4 sm:p-5 lg:p-6; }
.card-padding-lg { @apply p-6 sm:p-8 lg:p-10; }

/* Container */
.container-premium { @apply max-w-3xl mx-auto px-4 sm:px-6; }
.container-wide { @apply max-w-5xl mx-auto px-4 sm:px-6; }
.container-full { @apply max-w-7xl mx-auto px-4 sm:px-6; }

/* Grid gaps */
.gap-sm { @apply gap-2; }
.gap-md { @apply gap-3; }
.gap-lg { @apply gap-4; }
.gap-xl { @apply gap-6; }
```

---

## 11. Accessibility

### Reduced Motion Support
```css
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```

### Framer Motion Reduced Motion
```tsx
import { useReducedMotion } from "framer-motion";

export function AnimatedComponent() {
  const shouldReduceMotion = useReducedMotion();

  return (
    <motion.div
      animate={shouldReduceMotion ? {} : { opacity: 1, y: 0 }}
      transition={shouldReduceMotion ? { duration: 0 } : { duration: 0.5 }}
    >
      {/* Content */}
    </motion.div>
  );
}
```

### Focus Styles
```css
/* Focus visible */
.focus-visible:focus {
  @apply outline-none ring-2 ring-emerald-500/50 ring-offset-2 ring-offset-slate-900;
}

/* Skip to content */
.skip-link {
  @apply absolute -top-10 left-0 z-50 px-4 py-2 bg-emerald-500 text-white;
}
.skip-link:focus {
  @apply top-0;
}
```

---

## 12. Implementation Guide

### Step 1: Add Design Tokens to globals.css
```css
@layer base {
  :root {
    --glass-bg: rgba(255, 255, 255, 0.03);
    --glass-border: rgba(255, 255, 255, 0.06);
    --glass-blur: blur(12px);
  }
}
```

### Step 2: Create Shared Components
Create `src/components/ui/premium/` directory with:
- `glass-card.tsx`
- `animated-section.tsx`
- `score-ring.tsx`
- `stat-card.tsx`
- `section-header.tsx`
- `floating-input.tsx`
- `magnetic-button.tsx`

### Step 3: Add Animation Utilities
Create `src/lib/animations.ts` with all Framer Motion presets.

### Step 4: Update Existing Components
Replace existing components with premium versions:
- Wrap cards in `GlassCard`
- Add `ScrollRevealSection` to sections
- Use `PremiumScoreRing` instead of basic rings
- Add hover effects to interactive elements

### Step 5: Add CSS Animations
Add animation classes to `globals.css`:
- `.animate-reveal`
- `.animate-glow`
- `.animate-float`
- `.animate-shimmer`

---

## USAGE IN HANKITH NUMEROLOGY SOFTWARE

### Color Theme Application
```tsx
// All analysis pages use this consistent theme:
- Primary accent: emerald (green) - for positive scores, lucky numbers, success states
- Secondary accent: cyan (blue-green) - for neutral scores, information
- Tertiary accent: purple - for warnings, DOB-related features
- Background: slate-950 to slate-900 gradient
- Cards: glass effect with white/[0.03] background
- Borders: white/[0.06] for subtle separation
- Text: white/90 for headings, white/60 for body, white/40 for muted
```

### Animation Application
```tsx
// Page load: staggered fade-in from bottom
// Cards: hover lift effect with scale
// Scores: animated ring fill on mount
// Sections: scroll reveal with intersection observer
// Buttons: magnetic hover + ripple click
// Modals: scale + fade transition
// Lists: staggered children animation
```

---

## SELF-LEARNING SYSTEM

### Error Learning

- Track all errors encountered
- Analyze root causes
- Generate prevention rules
- Add test cases for errors
- Update knowledge base

### Usage Learning

- Monitor feature usage
- Identify popular features
- Detect unused features
- Optimize based on usage
- Add requested features

### Feedback Learning

- Collect user feedback
- Analyze feedback patterns
- Prioritize improvements
- Implement changes
- Verify improvements

### Knowledge Base

- Store best practices
- Store common solutions
- Store optimization techniques
- Store security patterns
- Store performance tips

### Cross-Project Updates

- Track improvements across projects
- Identify reusable patterns
- Propagate improvements globally
- Maintain consistency
- Share knowledge between skills

### Version Tracking

- Track all changes
- Document improvements
- Maintain changelog
- Enable rollback
- Support multiple versions

### Best Practice Updates

- Monitor industry trends
- Research new techniques
- Update skill accordingly
- Maintain compatibility
- Document changes

### Performance Monitoring

- Track execution time
- Monitor resource usage
- Identify bottlenecks
- Optimize performance
- Report improvements

---

**Remember**: Every animation should serve a purpose. Too many animations can overwhelm users. Use them strategically to guide attention and provide feedback.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
## FABEL5 DISCIPLINE (MANDATORY)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**This skill follows the Fabel5 six-phase senior-engineer loop.**

### Core Principle: THE MAKER IS NEVER THE GRADER

| Phase | Action |
|-------|--------|
| **1. THINK** | Map system, find source of truth, diagnose from real artifact |
| **2. DECOMPOSE** | Split into ONE bounded units, parallel where possible |
| **3. PROVE IT** | Build, run tests, validate — never claim without evidence |
| **4. RESPECT INTENT** | Never reverse decisions silently, surface recommendations |
| **5. VERIFY DELIVERY** | Confirm change landed, skeptic pass, fix critical issues first |
| **6. LEAVE NAVIGABLE** | Update notes, codify rules, write STATE.md |

### Evidence-Based Claims

| Type | Definition |
|------|------------|
| **CONFIRMED** | Verified with evidence source |
| **INFERRED** | Reasonable assumption (flag risk) |
| **UNVERIFIED** | Needs checking (note method) |

### Verification Vocabulary

- "should be" — expected state
- "to verify" — how to check
- "to ensure" — safety measures
- "to confirm" — validation
- "to make sure" — quality checks

### Final Instructions

1. Be skeptical — Find issues, dont confirm everything
2. Be thorough — Check every claim
3. Be honest — Say clearly if wrong
4. Be specific — Provide exact findings
5. Be constructive — Suggest fixes

