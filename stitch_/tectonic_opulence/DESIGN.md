---
name: Tectonic Opulence
colors:
  surface: '#fbf9f4'
  surface-dim: '#dbdad5'
  surface-bright: '#fbf9f4'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f5f3ee'
  surface-container: '#f0eee9'
  surface-container-high: '#eae8e3'
  surface-container-highest: '#e4e2dd'
  on-surface: '#1b1c19'
  on-surface-variant: '#46474a'
  inverse-surface: '#30312e'
  inverse-on-surface: '#f2f1ec'
  outline: '#76777b'
  outline-variant: '#c6c6cb'
  surface-tint: '#5e5e62'
  primary: '#060609'
  on-primary: '#ffffff'
  primary-container: '#1e1f22'
  on-primary-container: '#86868a'
  inverse-primary: '#c7c6ca'
  secondary: '#715b3c'
  on-secondary: '#ffffff'
  secondary-container: '#fddeb6'
  on-secondary-container: '#786041'
  tertiary: '#0b0601'
  on-tertiary: '#ffffff'
  tertiary-container: '#261e12'
  on-tertiary-container: '#928574'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e3e2e6'
  primary-fixed-dim: '#c7c6ca'
  on-primary-fixed: '#1a1b1e'
  on-primary-fixed-variant: '#46474a'
  secondary-fixed: '#fddeb6'
  secondary-fixed-dim: '#e0c29c'
  on-secondary-fixed: '#281802'
  on-secondary-fixed-variant: '#584326'
  tertiary-fixed: '#f0e0cc'
  tertiary-fixed-dim: '#d3c4b1'
  on-tertiary-fixed: '#221a0e'
  on-tertiary-fixed-variant: '#4f4537'
  background: '#fbf9f4'
  on-background: '#1b1c19'
  surface-variant: '#e4e2dd'
typography:
  display-xl:
    fontFamily: Noto Serif
    fontSize: 4rem
    fontWeight: '400'
    lineHeight: 4.5rem
    letterSpacing: -0.02em
  display-xl-mobile:
    fontFamily: Noto Serif
    fontSize: 2.5rem
    fontWeight: '400'
    lineHeight: 3rem
    letterSpacing: -0.01em
  headline-lg:
    fontFamily: Noto Serif
    fontSize: 2.5rem
    fontWeight: '400'
    lineHeight: 3rem
    letterSpacing: -0.015em
  headline-lg-mobile:
    fontFamily: Noto Serif
    fontSize: 1.75rem
    fontWeight: '400'
    lineHeight: 2.25rem
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Noto Serif
    fontSize: 1.75rem
    fontWeight: '500'
    lineHeight: 2.25rem
    letterSpacing: -0.01em
  headline-sm:
    fontFamily: Noto Serif
    fontSize: 1.25rem
    fontWeight: '500'
    lineHeight: 1.75rem
    letterSpacing: '0'
  title-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 1.125rem
    fontWeight: '600'
    lineHeight: 1.625rem
    letterSpacing: 0.01em
  body-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 1.125rem
    fontWeight: '300'
    lineHeight: 1.875rem
    letterSpacing: 0.01em
  body-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 0.9375rem
    fontWeight: '400'
    lineHeight: 1.6rem
    letterSpacing: '0'
  label-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 0.8125rem
    fontWeight: '600'
    lineHeight: 1.2rem
    letterSpacing: 0.08em
  label-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 0.75rem
    fontWeight: '500'
    lineHeight: 1rem
    letterSpacing: 0.12em
  spec-code:
    fontFamily: Plus Jakarta Sans
    fontSize: 0.6875rem
    fontWeight: '600'
    lineHeight: 0.875rem
    letterSpacing: 0.16em
spacing:
  gutter: 1.5rem
  gutter-desktop: 2.5rem
  margin: 1.25rem
  margin-tablet: 2.5rem
  margin-desktop: 4.5rem
  space-xs: 0.25rem
  space-sm: 0.5rem
  space-md: 1rem
  space-lg: 1.75rem
  space-xl: 3rem
---

## Brand & Style

This design system expresses the discipline of contemporary monumental architecture combined with the tactile warmth of quarried surfaces. Engineered for architects, interior visionaries, and discerning patrons, the interface evokes the sensation of stepping into an unadorned, high-ceilinged gallery of natural stone: deliberate, balanced, and uncompromisingly quiet.

The aesthetic fuses **Architectural Minimalism** with **Tactile Material Honesty**:
- Spatial proportion dictates visual hierarchy; elements breathe within generous stone-slab margins.
- Surface treatments evoke honed stone, polished travertine, and cold charcoal slate.
- Micro-details rely on hairline separations, metallic light catches, and precise typographic alignment.
- Bi-directional flow (LTR English and RTL Arabic) is treated symmetrically, upholding equal typographic authority and spatial elegance across scripts.

## Colors

The palette is derived from monumental geological strata, architectural mortars, and hand-rubbed brass inlays.

### Primary Palette
- **Deep Slate (`#1E1F22` - Primary)**: Pure monolithic weight. Used for principal typographic marks, primary navigational structures, and high-impact structural blocks.
- **Champagne Aurum (`#9E8462` - Secondary)**: A brushed, non-reflective metallic accent representing metal grout channels and brass hardware. Applied strictly to active states, rating badges, key actions, and selective borders.
- **Travertine Haze (`#B5A795` - Tertiary)**: Calcareous warm stone tone. Used for subtle structural borders, secondary iconography, and auxiliary text tiers.
- **Alabaster Calc (`#F7F5F0` - Neutral Canvas)**: Unbleached, warm mineral base serving as the default ground, providing warm light without clinical sterility.

### Surface Color Mapping
- **Surface Level 0 (Canvas)**: `#F7F5F0` (Alabaster Calc)
- **Surface Level 1 (Tile Slab/Card)**: `#FFFFFF` (Pure Calacatta)
- **Surface Level 2 (Recessed/Trough)**: `#EDE9E1` (Honed Mortar)
- **Surface Inverse (Curated Exhibition/Dark Slate)**: `#141517` with secondary `#CBB394`
- **Hairline Divider**: `rgba(30, 31, 34, 0.08)` on light; `rgba(247, 245, 240, 0.12)` on dark

## Typography

The typography system pairs classic editorial weight with modernist structural legibility.

### Latin & Arabic Pairing
- **Editorial Headlines**: `Noto Serif` paired with `Readex Pro` for Arabic headlines. This maintains classical proportions and high-end chiselled clarity.
- **Body & Specs**: `Plus Jakarta Sans` paired with `Readex Pro` for Arabic running text, technical schedules, and specifications.

### Rules of Typesetting
- Display and Headline tiers must remain strictly optical or low weight (`400` to `500`) to retain a carved, stone-mason feel. Never apply ultra-bold weights to architectural titles.
- Labels, dimension lines, and architectural specs use uppercase Latin tracking (`0.08em` to `0.16em`), countered in Arabic by balanced optical spacing without artificial letter breaks.
- Numerical specifications (e.g., `1200 × 2780 mm`, `9 mm thickness`, `PEI IV`) render tabular figures for aligned architectural manifests.

## Layout & Spacing

The layout is constructed around an architectural grid governed by structural ashlar joints and balance rather than dense packing.

### Grid Rhythm
- **Desktop (≥ 1280px)**: 12-column framework. `4.5rem` outer margins, `2.5rem` gutters. Maximum content bound capped at `1680px` for monumental panoramic presentations.
- **Tablet (768px – 1279px)**: 8-column layout. `2.5rem` margins, `1.5rem` gutters.
- **Mobile (< 768px)**: 4-column layout. `1.25rem` margins, `1rem` gutters.

### Component Spacing Principles
- Gaps between catalog items represent physical grout cuts: crisp, disciplined, and strictly uniform across vertical and horizontal planes.
- Section intervals prefer expansive negative space (`space-xl` to double `space-xl`) to establish an unhurried, luxury showroom tempo.

## Elevation & Depth

To reflect the flat, authentic surface quality of porcelain slabs, this design system avoids heavy drop shadows and simulated 3D volumes. Depth is established through **architectural layering, crisp hairline boundaries, and ambient grazing light**.

### Depth Layers
- **Ground Floor (Base Canvas)**: Zero elevation, finished in `#F7F5F0`.
- **Raised Stone (Interactive Cards & Drawers)**: 1px structural border in `#1E1F22` at 8% opacity. Layered over pure white `#FFFFFF` with an ambient ground shadow: `0 8px 32px -4px rgba(30, 31, 34, 0.04)`.
- **Floating Inspection (Sample Viewer, Lightbox, Material Spec Sheets)**: Elevated panel surrounded by a distinct 1px border in `#9E8462` (Champagne Aurum) at 30% opacity, backdropped by an ambient floor haze: `0 24px 64px -12px rgba(30, 31, 34, 0.12)`.
- **Recessed Inset (Slab Cutouts & Filter Wells)**: `#EDE9E1` solid background with an inner keyline (`inset 0 1px 2px rgba(30, 31, 34, 0.04)`), simulating carved limestone.

## Shapes

The design system embraces an absolute architectural edge profile: **Level 0 (Sharp)**.

### Geometric Discipline
- Every card, button, badge, input, and modal features **0px border radius**, reflecting rectified porcelain slabs, dimensional pavers, and cut stone blocks.
- Internal dividers, thumbnail viewports, and interactive swatches must remain precisely perpendicular.
- The sole circular exceptions are reserved for material finish samples (the tactile round swatch) and minimal status indicators.

## Components

### Buttons
- **Primary Slab Button**: Solid `#1E1F22` background, `#F7F5F0` text, 0px radius, uppercase tracked typography (`label-lg`). Hover transition reveals a subtle `#9E8462` 1px inset bottom edge with minimal surface translation.
- **Secondary Aurum Outline**: Transparent ground, 1px solid `#9E8462` border, `#1E1F22` text. Hover state shifts surface to `#9E8462` with `#FFFFFF` text.
- **Text Action (Editorial Link)**: Plain text accompanied by a hairline arrow, underlined with a 1px border spaced 6px below baseline. Underline extends smoothly on hover.

### Architectural Chips & Badges
- **Specification Badges (PEI Rating & Slip Resistance)**:
  - Compact rectilinear boxes (`24px` height).
  - Background `#EDE9E1`, 1px solid border `#B5A795`.
  - Monospaced numeric alignment (`spec-code`): e.g., `PEI IV`, `R11 / C`, `V2 SLIGHT`.
- **Surface Finish Badges (Polished, Matt, Satin, Grip)**:
  - Displayed in uppercase `label-md`.
  - Paired with an interactive micro-texture preview icon or indicator.
  - Active state framed in solid `#9E8462` with crisp white text.

### Material Cards (Tile & Slab Displays)
- Unframed Calacatta White ground (`#FFFFFF`) or enclosed within hairline grid borders.
- Top visual: high-resolution material tile showing vein patterns with aspect ratio locked to production dimensions (e.g., 1:1, 1:2, 1:3 for big slabs).
- Bottom metadata tray: slab name in `Noto Serif` / `Readex Pro`, dimension formula (e.g., `120×280 cm`), accompanied by a flush row of technical chips (Finish, R-rating, Thickness).

### Form Controls & Inputs
- **Text Fields**: Clean single hairline baseline (`1px solid #B5A795`) on `#F7F5F0` or boxed fields with 1px border. Label shifts smoothly upward to `label-md` on focus; border transitions to `#1E1F22` or `#9E8462`.
- **Checkboxes & Radios**: Monolithic squares (`16px × 16px`), sharp corners. Unchecked: 1px border `#B5A795`. Checked: solid `#1E1F22` fill with a sharp centered brass-gold tick or inner square.

### Lists & Architectural Schedules
- Tabular format designed like stone-mason billing schedules.
- Alternating subtle rows (`#F7F5F0` and `#FFFFFF`) divided by `1px solid rgba(30, 31, 34, 0.06)`.
- Monospace-aligned measurements, finish designations, and batch tonnage.

### Bilingual Mirroring Architecture
- Layout flows seamlessly in RTL (`dir="rtl"`) without structural shift: the right-hand column anchors project manifests, specifications align systematically to the right edge, and hairline accents track inward toward the focal element.