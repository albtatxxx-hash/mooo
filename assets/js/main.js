/**
 * Main Application Script for Porcelana Larin
 * Handles Navigation, Sample Drawer, Toasts, Copy-to-Clipboard,
 * Countdown Timers, Lighting Simulator & Mobile UX.
 */

// Global State for Sample Drawer
const SampleManager = {
  items: [
    {
      id: 'calacatta-royal',
      name: 'بورسلين كالاكاتا رويال الإيطالي',
      size: '120×280 سم',
      finish: 'لامع ومصقول (Polished)',
      img: 'https://lh3.googleusercontent.com/aida-public/AB6AXuDFwmBG3cQJPJXFlG-AmIfXvdAj22IHIYQtj5RpWpUfi9B_Pw8GRPU2giSb8p8dNr7GhPRaJ6L8kBVIe3fxtdRix2ZlrE9itmrolE4lNL9rQtDy-YHFfmBuDf09hLhYohYjJ03zPbTCr_8MuaXc9qp-2iteTXJVJCNW997ttN2Fd26vSo-Rmx2l2UcdLa1whdicUR_lfD3-zkDYdNvHaE9_-KC_osG-sYLYbaT31O1t'
    },
    {
      id: 'marquina-black',
      name: 'بورسلين نيرو ماركينا الفاخر',
      size: '80×160 سم',
      finish: 'شبه لامع (Lappato)',
      img: 'https://lh3.googleusercontent.com/aida-public/AB6AXuDYhYg5hK118n4H09eBsq0k8F44jFw6rN0z5e2x-gY6sH7kL0eD3o0mF5j-qF4pG8hT9mQ1w2e3r4t5'
    }
  ],

  init() {
    this.updateUI();
  },

  add(item) {
    if (this.items.length >= 3) {
      showToast('الحد الأقصى هو 3 عينات مجانية لكل طلب!', 'info');
      this.openDrawer();
      return;
    }
    const exists = this.items.some(i => i.id === item.id);
    if (exists) {
      showToast('هذه العينة مضافة بالفعل في سلة العينات!', 'info');
      this.openDrawer();
      return;
    }
    this.items.push(item);
    this.updateUI();
    showToast(`تمت إضافة "${item.name}" إلى صندوق العينات!`, 'check_circle');
    this.openDrawer();
  },

  remove(index) {
    if (index >= 0 && index < this.items.length) {
      const removed = this.items.splice(index, 1);
      this.updateUI();
      showToast(`تم حذف العينة بنجاح`, 'delete');
    }
  },

  updateUI() {
    // Update badge counters
    const badges = document.querySelectorAll('.sample-count-badge');
    badges.forEach(b => {
      b.textContent = `${this.items.length} عينات`;
    });

    const numBadges = document.querySelectorAll('.sample-count-num');
    numBadges.forEach(b => {
      b.textContent = this.items.length;
    });

    // Update Drawer List
    const listEl = document.getElementById('sample-drawer-list');
    const emptyEl = document.getElementById('sample-drawer-empty');
    const footerEl = document.getElementById('sample-drawer-footer');

    if (listEl) {
      if (this.items.length === 0) {
        listEl.innerHTML = '';
        if (emptyEl) emptyEl.classList.remove('hidden');
        if (footerEl) footerEl.classList.add('hidden');
      } else {
        if (emptyEl) emptyEl.classList.add('hidden');
        if (footerEl) footerEl.classList.remove('hidden');

        listEl.innerHTML = this.items.map((item, idx) => `
          <div class="flex items-center justify-between p-3 bg-surface-container rounded-lg border border-outline-variant/30 transition-all hover:border-secondary/50">
            <div class="flex items-center gap-3">
              <div class="w-14 h-14 rounded overflow-hidden shrink-0 bg-surface-container-high border border-outline-variant/40">
                <img src="${item.img || 'https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=200&q=80'}" alt="${item.name}" class="w-full h-full object-cover">
              </div>
              <div class="flex flex-col">
                <span class="font-bold text-on-surface text-sm line-clamp-1">${item.name}</span>
                <span class="text-xs text-on-surface-variant">${item.size} • ${item.finish}</span>
                <span class="text-[11px] text-secondary font-semibold mt-0.5">عينة مجانية مختارة</span>
              </div>
            </div>
            <button onclick="SampleManager.remove(${idx})" class="text-error hover:bg-error-container/40 p-1.5 rounded transition-colors" title="حذف العينة">
              <span class="material-symbols-outlined text-[18px]">close</span>
            </button>
          </div>
        `).join('');
      }
    }
  },

  openDrawer() {
    const drawer = document.getElementById('sample-drawer');
    const backdrop = document.getElementById('drawer-backdrop');
    if (drawer && backdrop) {
      drawer.classList.add('active');
      backdrop.classList.add('active');
      document.body.style.overflow = 'hidden';
    }
  },

  closeDrawer() {
    const drawer = document.getElementById('sample-drawer');
    const backdrop = document.getElementById('drawer-backdrop');
    if (drawer && backdrop) {
      drawer.classList.remove('active');
      backdrop.classList.remove('active');
      document.body.style.overflow = '';
    }
  }
};

// Global Toast System
function showToast(message, icon = 'check_circle') {
  let container = document.getElementById('toast-container');
  if (!container) {
    container = document.createElement('div');
    container.id = 'toast-container';
    document.body.appendChild(container);
  }

  const toast = document.createElement('div');
  toast.className = 'toast-item';
  toast.innerHTML = `
    <span class="material-symbols-outlined text-secondary-fixed text-[22px]">${icon}</span>
    <span>${message}</span>
  `;

  container.appendChild(toast);

  setTimeout(() => {
    toast.classList.add('removing');
    setTimeout(() => {
      if (toast.parentElement) toast.remove();
    }, 260);
  }, 3500);
}

// Copy to Clipboard Utility
function copyMarketingText(textOrElemId, customMsg = 'تم نسخ النص الترويجي بنجاح!') {
  let content = '';
  const elem = document.getElementById(textOrElemId);
  if (elem) {
    content = elem.innerText || elem.textContent;
  } else {
    content = textOrElemId;
  }

  if (navigator.clipboard && navigator.clipboard.writeText) {
    navigator.clipboard.writeText(content).then(() => {
      showToast(customMsg, 'content_copy');
    }).catch(() => {
      fallbackCopy(content, customMsg);
    });
  } else {
    fallbackCopy(content, customMsg);
  }
}

function fallbackCopy(text, customMsg) {
  const textarea = document.createElement('textarea');
  textarea.value = text;
  textarea.style.position = 'fixed';
  textarea.style.opacity = '0';
  document.body.appendChild(textarea);
  textarea.select();
  try {
    document.execCommand('copy');
    showToast(customMsg, 'content_copy');
  } catch (err) {
    showToast('تعذر النسخ التلقائي، يرجى التحديد والنسخ يدوياً', 'warning');
  }
  document.body.removeChild(textarea);
}

// Mobile Menu Navigation
function toggleMobileMenu() {
  const menu = document.getElementById('mobile-menu-drawer');
  const backdrop = document.getElementById('mobile-menu-backdrop');
  if (!menu || !backdrop) return;

  const isActive = menu.classList.contains('active');
  if (isActive) {
    closeMobileMenu();
  } else {
    menu.classList.add('active');
    backdrop.classList.add('active');
    document.body.style.overflow = 'hidden';
  }
}

function closeMobileMenu() {
  const menu = document.getElementById('mobile-menu-drawer');
  const backdrop = document.getElementById('mobile-menu-backdrop');
  if (menu) menu.classList.remove('active');
  if (backdrop) backdrop.classList.remove('active');
  document.body.style.overflow = '';
}

// Direct WhatsApp Link Helper
function openWhatsAppWithText(message) {
  const phone = '966920000000'; // Default Showroom Central line
  const url = `https://wa.me/${phone}?text=${encodeURIComponent(message)}`;
  window.open(url, '_blank');
}

// Live Countdown Timer for Campaign Models
function initCountdown(targetDateStr, containerId = 'offer-countdown') {
  const container = document.getElementById(containerId);
  if (!container) return;

  // If no date provided, set target to 7 days from now
  let target = new Date(targetDateStr).getTime();
  if (isNaN(target)) {
    target = new Date().getTime() + (7 * 24 * 60 * 60 * 1000);
  }

  function update() {
    const now = new Date().getTime();
    const distance = target - now;

    if (distance < 0) {
      container.innerHTML = '<span class="text-error font-bold">انتهت فترة العرض الحصري! ترقبوا التحديث القادم.</span>';
      return;
    }

    const days = Math.floor(distance / (1000 * 60 * 60 * 24));
    const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((distance % (1000 * 60)) / 1000);

    const dEl = document.getElementById('cd-days');
    const hEl = document.getElementById('cd-hours');
    const mEl = document.getElementById('cd-minutes');
    const sEl = document.getElementById('cd-seconds');

    if (dEl) dEl.textContent = String(days).padStart(2, '0');
    if (hEl) hEl.textContent = String(hours).padStart(2, '0');
    if (mEl) mEl.textContent = String(minutes).padStart(2, '0');
    if (sEl) sEl.textContent = String(seconds).padStart(2, '0');
  }

  update();
  setInterval(update, 1000);
}

// Lighting & Motion Simulator for Porcelain Tile
function updateLightingReflection(val) {
  const glare = document.getElementById('porcelain-glare');
  const lightLabel = document.getElementById('light-angle-label');
  const tileStage = document.getElementById('lighting-tile-stage');

  if (glare) {
    const angle = Number(val);
    if (lightLabel) lightLabel.textContent = `${angle}°`;
    const posX = angle;
    const posY = Math.sin((angle * Math.PI) / 180) * 50 + 50;
    glare.style.background = `radial-gradient(circle at ${posX}% ${posY}%, rgba(255,255,255,0.75) 0%, rgba(255,255,255,0.2) 35%, rgba(0,0,0,0) 70%)`;
  }

  if (tileStage) {
    // Add dynamic shine pulse
    tileStage.classList.add('active-shine');
    setTimeout(() => tileStage.classList.remove('active-shine'), 1200);
  }
}

// Motion Quick Cut Simulator
let motionInterval = null;
function toggleMotionPreview() {
  const motionBtn = document.getElementById('motion-toggle-btn');
  const tileStage = document.getElementById('lighting-tile-stage');
  const motionStatus = document.getElementById('motion-status-text');

  if (!tileStage) return;

  if (motionInterval) {
    clearInterval(motionInterval);
    motionInterval = null;
    if (motionBtn) {
      motionBtn.innerHTML = '<span class="material-symbols-outlined text-[18px]">play_arrow</span><span>تشغيل لقطات الموشن السريعة</span>';
      motionBtn.classList.remove('bg-error', 'text-white');
      motionBtn.classList.add('bg-primary', 'text-on-primary');
    }
    if (motionStatus) motionStatus.textContent = 'المحاكاة متوقفة';
  } else {
    let angle = 10;
    motionInterval = setInterval(() => {
      angle = (angle + 35) % 100;
      updateLightingReflection(angle);
      const slider = document.getElementById('light-slider');
      if (slider) slider.value = angle;
    }, 450);

    if (motionBtn) {
      motionBtn.innerHTML = '<span class="material-symbols-outlined text-[18px]">pause</span><span>إيقاف الموشن</span>';
      motionBtn.classList.remove('bg-primary', 'text-on-primary');
      motionBtn.classList.add('bg-error', 'text-white');
    }
    if (motionStatus) motionStatus.textContent = 'جاري المحاكاة: لقطات سريعة وإضاءة متحركة';
  }
}

// Highlight Current Active Page in Navigation
function highlightActiveNavigation() {
  const currentPath = window.location.pathname.split('/').pop() || 'index.html';
  const navLinks = document.querySelectorAll('header nav a, .side-drawer nav a, .mobile-bottom-bar a');

  navLinks.forEach(link => {
    const href = link.getAttribute('href');
    if (!href) return;
    const linkPath = href.split('#')[0];

    if (linkPath === currentPath || (currentPath === '' && linkPath === 'index.html')) {
      link.classList.add('bg-secondary-container', 'text-on-secondary-container', 'font-semibold');
      link.classList.remove('text-on-surface-variant');
    }
  });
}

// Initialize on DOM Ready
document.addEventListener('DOMContentLoaded', () => {
  SampleManager.init();
  highlightActiveNavigation();

  // Attach sample tray trigger buttons
  document.querySelectorAll('[data-action="open-samples"]').forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      SampleManager.openDrawer();
    });
  });

  // Attach mobile menu trigger buttons
  document.querySelectorAll('[data-action="toggle-mobile-menu"]').forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      toggleMobileMenu();
    });
  });

  // Attach copy buttons
  document.querySelectorAll('[data-copy-target]').forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const targetId = btn.getAttribute('data-copy-target');
      const customMsg = btn.getAttribute('data-copy-msg') || 'تم نسخ النص بنجاح!';
      copyMarketingText(targetId, customMsg);
    });
  });
});
