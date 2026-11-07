import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

# Read source files
with open('stitch_/_2/code.html', 'r', encoding='utf-8') as f:
    home_src = f.read()

with open('stitch_/_3/code.html', 'r', encoding='utf-8') as f:
    catalog_src = f.read()

with open('stitch_/_4/code.html', 'r', encoding='utf-8') as f:
    product_src = f.read()

with open('stitch_/_5/code.html', 'r', encoding='utf-8') as f:
    consultation_src = f.read()

# Common Unified Header
def get_unified_header(active_page):
    return f'''
  <!-- Top Announcement Bar -->
  <div class="w-full bg-primary text-on-primary py-2 px-4 md:px-12 text-center shadow-sm">
    <div class="max-w-[1680px] mx-auto flex flex-wrap items-center justify-between text-xs tracking-wider text-surface-container-high gap-2">
      <div class="flex items-center gap-2">
        <span class="inline-flex items-center gap-1 bg-secondary text-white text-[11px] px-2 py-0.5 rounded font-bold">عروض 2025</span>
        <span>خدمة شحن عينات للمنازل مجاناً</span>
        <span class="text-secondary-fixed-dim">|</span>
        <a href="promos.html#model-offers" class="hover:text-secondary-fixed underline underline-offset-4 decoration-secondary text-secondary-fixed">خصومات حصرية للفرز الأول وعروض تشطيب الشقق الكاملة 🔥</a>
      </div>
      <div class="flex items-center gap-4 text-xs">
        <div class="flex items-center gap-1">
          <span class="material-symbols-outlined text-[16px] text-secondary">schedule</span>
          <span>مواعيد العمل: 9:00 ص - 10:00 م</span>
        </div>
        <div class="flex items-center gap-1">
          <span class="text-secondary-fixed-dim">هاتف المعرض:</span>
          <a href="tel:920000000" class="font-bold text-white hover:text-secondary-fixed" dir="ltr">920000000</a>
        </div>
      </div>
    </div>
  </div>

  <!-- Header Navigation -->
  <header class="w-full bg-surface/95 backdrop-blur-xl shadow-sm sticky top-0 z-50 border-b border-outline-variant/30">
    <div class="h-20 max-w-[1680px] mx-auto px-4 md:px-12 flex items-center justify-between gap-6">
      <!-- Logo -->
      <a href="index.html" class="flex items-center gap-3 shrink-0 group">
        <img alt="Porcelana Larin Logo" class="h-9 w-auto object-contain transition-transform group-hover:scale-105" src="https://lh3.googleusercontent.com/aida/ALJJyrBT7sUfgy8qGADX3DbzAbvgi485MnM2z-mbLx3idJsz4ONfCBj0fYdFL8zsvgbuPkS-Oz50FEURwW_umNpnZDhZIGpV7YNw6y8l87XVHS9IBqDR4LRl9MUpxJ3ikvEHRsnmfpbjBS56UckmPro5A9s39dx0B3nYj-orjc_KuaFA8z88ZMo5aC_eJIs_4g06zI2sTdjByjDjbW1xSTw96qo-M7XyDe5MfFZvWrB6Q4CF_w"/>
        <div class="flex flex-col">
          <span class="font-headline text-lg text-primary tracking-tight font-bold">بورسلانا لارين</span>
          <span class="text-[10px] text-on-surface-variant tracking-widest uppercase">معرض البورسلين والسيراميك الفاخر</span>
        </div>
      </a>

      <!-- Desktop Nav -->
      <nav class="hidden lg:flex items-center gap-1 xl:gap-2">
        <a href="index.html" class="px-3.5 py-1.5 rounded text-sm {'bg-secondary-container text-on-secondary-container font-bold' if active_page == 'home' else 'text-on-surface-variant hover:text-primary transition-colors'}">الرئيسية</a>
        <a href="catalog.html" class="px-3.5 py-1.5 rounded text-sm {'bg-secondary-container text-on-secondary-container font-bold' if active_page == 'catalog' else 'text-on-surface-variant hover:text-primary transition-colors'}">كتالوج المنتجات</a>
        <a href="product.html" class="px-3.5 py-1.5 rounded text-sm {'bg-secondary-container text-on-secondary-container font-bold' if active_page == 'product' else 'text-on-surface-variant hover:text-primary transition-colors'}">تفاصيل البورسلين</a>
        <a href="promos.html" class="px-3.5 py-1.5 rounded text-sm flex items-center gap-1.5 {'bg-secondary-container text-on-secondary-container font-bold' if active_page == 'promos' else 'text-on-surface-variant hover:text-primary transition-colors'}">
          <span>الحملات والعروض</span>
          <span class="bg-secondary text-white text-[10px] px-1.5 py-0.2 rounded-full font-bold">3 نماذج</span>
        </a>
        <a href="consultation.html" class="px-3.5 py-1.5 rounded text-sm {'bg-secondary-container text-on-secondary-container font-bold' if active_page == 'consultation' else 'text-on-surface-variant hover:text-primary transition-colors'}">الاستشارة الهندسية</a>
      </nav>

      <!-- Actions -->
      <div class="flex items-center gap-3">
        <a href="catalog.html" class="hidden xl:flex items-center bg-surface-container hover:bg-surface-container-high px-3 py-1.5 gap-2 rounded transition-colors text-xs text-on-surface-variant">
          <span class="material-symbols-outlined text-[16px]">search</span>
          <span>بحث عن رخام، بورسلان...</span>
        </a>
        <button data-action="open-samples" class="relative flex items-center gap-1.5 bg-surface-container-high hover:bg-surface-container-highest px-3 py-2 transition-colors rounded text-xs font-semibold cursor-pointer">
          <span class="material-symbols-outlined text-primary text-[18px]">grid_view</span>
          <span class="sample-count-badge">3 عينات</span>
          <span class="w-2 h-2 rounded-full bg-secondary absolute -top-1 -right-1 animate-ping"></span>
        </button>
        <a href="consultation.html" class="hidden sm:inline-flex bg-primary text-on-primary hover:bg-secondary hover:text-white px-4 py-2 rounded text-xs font-bold transition-all">
          احجز استشارة مجانية
        </a>
        <button data-action="toggle-mobile-menu" class="lg:hidden p-2 text-primary hover:bg-surface-container-high rounded" aria-label="القائمة">
          <span class="material-symbols-outlined text-[24px]">menu</span>
        </button>
      </div>
    </div>
  </header>
'''

# Common Unified Footer
def get_unified_footer():
    return '''
  <!-- Unified Luxury Footer -->
  <footer class="w-full bg-surface-container-low text-on-surface border-t border-outline-variant/30 mt-20">
    <div class="max-w-[1680px] mx-auto px-4 md:px-12 py-12">
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8 mb-10">
        <!-- Col 1 -->
        <div class="flex flex-col gap-3">
          <div class="flex items-center gap-2">
            <img alt="Porcelana Larin" class="h-8 w-auto" src="https://lh3.googleusercontent.com/aida/ALJJyrBT7sUfgy8qGADX3DbzAbvgi485MnM2z-mbLx3idJsz4ONfCBj0fYdFL8zsvgbuPkS-Oz50FEURwW_umNpnZDhZIGpV7YNw6y8l87XVHS9IBqDR4LRl9MUpxJ3ikvEHRsnmfpbjBS56UckmPro5A9s39dx0B3nYj-orjc_KuaFA8z88ZMo5aC_eJIs_4g06zI2sTdjByjDjbW1xSTw96qo-M7XyDe5MfFZvWrB6Q4CF_w"/>
            <span class="font-headline text-lg font-bold text-primary">بورسلانا لارين</span>
          </div>
          <p class="text-xs text-on-surface-variant leading-relaxed">
            صرح معماري رائد يوفر ألواح البورسلان الإيطالية والإسبانية الفاخرة للقصور، الفلل، والمشاريع السكنية والتجارية الاستثنائية.
          </p>
          <div class="flex items-center gap-2 text-xs font-semibold text-secondary">
            <span>فرز أول معتمد</span>
            <span>•</span>
            <span>ضمان 10 سنوات</span>
            <span>•</span>
            <span>عزل ونقاء فائق</span>
          </div>
        </div>

        <!-- Col 2: Navigation Links -->
        <div class="flex flex-col gap-2">
          <span class="font-bold text-primary text-sm mb-1">أقسام الموقع</span>
          <a href="index.html" class="text-xs text-on-surface-variant hover:text-secondary transition-colors">الصفحة الرئيسية</a>
          <a href="catalog.html" class="text-xs text-on-surface-variant hover:text-secondary transition-colors">كتالوج البورسلين 2025</a>
          <a href="product.html" class="text-xs text-on-surface-variant hover:text-secondary transition-colors">تفاصيل البورسلين وحاسبة الأمتار</a>
          <a href="consultation.html" class="text-xs text-on-surface-variant hover:text-secondary transition-colors">طلب استشارة ومعاينة ميدانية</a>
          <a href="promos.html" class="text-xs font-bold text-secondary hover:underline">مركز الحملات الإعلانية (3 نماذج)</a>
        </div>

        <!-- Col 3: Promos Directly -->
        <div class="flex flex-col gap-2">
          <span class="font-bold text-primary text-sm mb-1">نماذج الحملات والبرومو</span>
          <a href="promos.html#model-social" class="text-xs text-on-surface-variant hover:text-secondary transition-colors">1. نموذج السوشيال ميديا والريلز</a>
          <a href="promos.html#model-offers" class="text-xs text-on-surface-variant hover:text-secondary transition-colors">2. نموذج عروض الافتتاح وتخفيضات العرسان 🔥</a>
          <a href="promos.html#model-luxury" class="text-xs text-on-surface-variant hover:text-secondary transition-colors">3. نموذج الفلل والديكورات الفاخرة 💎</a>
          <a href="promos.html#model-motion-tip" class="text-xs text-on-surface-variant hover:text-secondary transition-colors">نصيحة نجاح البرومو ومختبر الموشن</a>
        </div>

        <!-- Col 4: Contact & Showrooms -->
        <div class="flex flex-col gap-2">
          <span class="font-bold text-primary text-sm mb-1">تواصل مع المعرض</span>
          <div class="text-xs text-on-surface-variant flex items-center gap-2">
            <span class="material-symbols-outlined text-[16px] text-secondary">location_on</span>
            <span>طريق التخصصي، حي المحمدية، الرياض</span>
          </div>
          <div class="text-xs text-on-surface-variant flex items-center gap-2">
            <span class="material-symbols-outlined text-[16px] text-secondary">call</span>
            <a href="tel:920000000" dir="ltr" class="font-bold hover:text-secondary">920000000</a>
          </div>
          <div class="text-xs text-on-surface-variant flex items-center gap-2">
            <span class="material-symbols-outlined text-[16px] text-secondary">schedule</span>
            <span>9:00 ص - 10:00 م يومياً</span>
          </div>
        </div>
      </div>

      <div class="pt-6 border-t border-outline-variant/30 flex flex-wrap items-center justify-between text-xs text-on-surface-variant gap-4">
        <span>© 2025 بورسلانا لارين. جميع الحقوق محفوظة.</span>
        <div class="flex items-center gap-4">
          <a href="index.html" class="hover:text-secondary">الرئيسية</a>
          <span>•</span>
          <a href="catalog.html" class="hover:text-secondary">الكتالوج</a>
          <span>•</span>
          <a href="product.html" class="hover:text-secondary">المنتج</a>
          <span>•</span>
          <a href="consultation.html" class="hover:text-secondary">الاستشارة</a>
          <span>•</span>
          <a href="promos.html" class="hover:text-secondary font-bold">الحملات</a>
        </div>
      </div>
    </div>
  </footer>

  <!-- Sample Drawer -->
  <div id="drawer-backdrop" class="drawer-backdrop" onclick="SampleManager.closeDrawer()"></div>
  <div id="sample-drawer" class="side-drawer">
    <div class="p-5 border-b border-outline-variant/30 flex items-center justify-between bg-surface-container">
      <div class="flex items-center gap-2">
        <span class="material-symbols-outlined text-secondary text-[24px]">grid_view</span>
        <div>
          <h3 class="font-bold text-primary text-base">صندوق العينات المجاني</h3>
          <p class="text-xs text-on-surface-variant">اختر حتى 3 عينات مجانية لمعاينتها في منزلك</p>
        </div>
      </div>
      <button onclick="SampleManager.closeDrawer()" class="p-1 rounded text-on-surface-variant hover:text-on-surface hover:bg-surface-container-high">
        <span class="material-symbols-outlined text-[22px]">close</span>
      </button>
    </div>
    <div class="flex-1 overflow-y-auto p-5 flex flex-col gap-3">
      <div id="sample-drawer-empty" class="hidden flex flex-col items-center justify-center py-16 text-center">
        <span class="material-symbols-outlined text-outline text-[48px] mb-2">dashboard_customize</span>
        <p class="font-bold text-on-surface">صندوق العينات فارغ حالياً</p>
        <p class="text-xs text-on-surface-variant mt-1 max-w-[240px]">تصفح الكتالوج واختر حتى 3 عينات لتصلك حتى باب بيتك مجاناً</p>
        <a href="catalog.html" onclick="SampleManager.closeDrawer()" class="mt-4 bg-primary text-on-primary px-4 py-2 text-xs font-semibold rounded hover:bg-secondary">استعراض الكتالوج</a>
      </div>
      <div id="sample-drawer-list" class="flex flex-col gap-3"></div>
    </div>
    <div id="sample-drawer-footer" class="p-5 border-t border-outline-variant/30 bg-surface-container-low flex flex-col gap-3">
      <div class="flex items-center justify-between text-xs text-on-surface-variant">
        <span>رسوم التوصيل والتحضير:</span>
        <span class="font-bold text-secondary text-sm">مجاناً 100%</span>
      </div>
      <a href="consultation.html?type=samples" onclick="SampleManager.closeDrawer()" class="w-full bg-primary text-on-primary text-center py-3 rounded font-bold hover:bg-secondary transition-colors flex items-center justify-center gap-2">
        <span class="material-symbols-outlined text-[18px]">local_shipping</span>
        <span>تأكيد طلب شحن العينات للمنزل</span>
      </a>
    </div>
  </div>

  <!-- Mobile Drawer Menu -->
  <div id="mobile-menu-backdrop" class="drawer-backdrop" onclick="closeMobileMenu()"></div>
  <div id="mobile-menu-drawer" class="side-drawer">
    <div class="p-5 border-b border-outline-variant/30 flex items-center justify-between bg-surface-container">
      <div class="flex items-center gap-2">
        <img alt="Porcelana Larin" class="h-7 w-auto" src="https://lh3.googleusercontent.com/aida/ALJJyrBT7sUfgy8qGADX3DbzAbvgi485MnM2z-mbLx3idJsz4ONfCBj0fYdFL8zsvgbuPkS-Oz50FEURwW_umNpnZDhZIGpV7YNw6y8l87XVHS9IBqDR4LRl9MUpxJ3ikvEHRsnmfpbjBS56UckmPro5A9s39dx0B3nYj-orjc_KuaFA8z88ZMo5aC_eJIs_4g06zI2sTdjByjDjbW1xSTw96qo-M7XyDe5MfFZvWrB6Q4CF_w"/>
        <span class="font-bold text-primary">بورسلانا لارين</span>
      </div>
      <button onclick="closeMobileMenu()" class="p-1 rounded text-on-surface-variant hover:text-on-surface hover:bg-surface-container-high">
        <span class="material-symbols-outlined text-[22px]">close</span>
      </button>
    </div>
    <div class="flex-1 overflow-y-auto p-5 flex flex-col gap-2">
      <a href="index.html" class="flex items-center justify-between p-3 rounded-lg hover:bg-surface-container font-semibold text-on-surface">
        <div class="flex items-center gap-3">
          <span class="material-symbols-outlined text-secondary">home</span>
          <span>الرئيسية</span>
        </div>
        <span class="material-symbols-outlined text-outline text-[18px]">chevron_left</span>
      </a>
      <a href="catalog.html" class="flex items-center justify-between p-3 rounded-lg hover:bg-surface-container font-semibold text-on-surface">
        <div class="flex items-center gap-3">
          <span class="material-symbols-outlined text-secondary">category</span>
          <span>كتالوج المنتجات 2025</span>
        </div>
        <span class="material-symbols-outlined text-outline text-[18px]">chevron_left</span>
      </a>
      <a href="product.html" class="flex items-center justify-between p-3 rounded-lg hover:bg-surface-container font-semibold text-on-surface">
        <div class="flex items-center gap-3">
          <span class="material-symbols-outlined text-secondary">view_in_ar</span>
          <span>تفاصيل البورسلين والحاسبة</span>
        </div>
        <span class="material-symbols-outlined text-outline text-[18px]">chevron_left</span>
      </a>
      <a href="promos.html" class="flex items-center justify-between p-3 rounded-lg bg-secondary-container text-on-secondary-container font-bold">
        <div class="flex items-center gap-3">
          <span class="material-symbols-outlined text-secondary">campaign</span>
          <span>مركز النماذج الإعلانية (3 نماذج)</span>
        </div>
        <span class="material-symbols-outlined text-secondary text-[18px]">chevron_left</span>
      </a>
      <a href="promo-social.html" class="p-2.5 rounded text-xs text-on-surface-variant hover:bg-surface-container pr-8 block">
        • 1. نموذج السوشيال ميديا والريلز
      </a>
      <a href="promo-offers.html" class="p-2.5 rounded text-xs text-on-surface-variant hover:bg-surface-container pr-8 block">
        • 2. نموذج عروض الافتتاح والفرز الأول 🔥
      </a>
      <a href="promo-luxury.html" class="p-2.5 rounded text-xs text-on-surface-variant hover:bg-surface-container pr-8 block">
        • 3. نموذج الفلل والديكورات الفاخرة 💎
      </a>
      <a href="consultation.html" class="flex items-center justify-between p-3 rounded-lg hover:bg-surface-container font-semibold text-on-surface mt-2">
        <div class="flex items-center gap-3">
          <span class="material-symbols-outlined text-secondary">support_agent</span>
          <span>طلب استشارة ومعاينة هندسية</span>
        </div>
        <span class="material-symbols-outlined text-outline text-[18px]">chevron_left</span>
      </a>
    </div>
    <div class="p-5 border-t border-outline-variant/30 bg-surface-container-low flex flex-col gap-2">
      <a href="tel:920000000" class="w-full bg-primary text-on-primary text-center py-2.5 rounded font-bold flex items-center justify-center gap-2">
        <span class="material-symbols-outlined text-[18px]">call</span>
        <span dir="ltr">920000000</span>
      </a>
      <button onclick="openWhatsAppWithText('مرحباً، أود الاستفسار عن عروض وتشكيلة البورسلين والسيراميك')" class="w-full bg-[#25D366] text-white text-center py-2.5 rounded font-bold flex items-center justify-center gap-2">
        <span class="material-symbols-outlined text-[18px]">chat</span>
        <span>محادثة واتساب مباشرة</span>
      </button>
    </div>
  </div>

  <!-- Floating WhatsApp -->
  <a href="https://wa.me/966920000000?text=%D9%85%D8%B1%D8%AD%D8%A8%D8%A7%D9%8B%D8%8C%20%D8%A3%D9%88%D8%AF%20%D8%A7%D9%84%D8%A7%D8%B3%D8%AA%D9%81%D8%B3%D8%A7%D8%B1%20%D8%B9%D9%86%20%D8%AA%D8%B4%D9%83%D9%8A%D9%84%D8%A9%20%D8%A7%D9%84%D8%A8%D9%88%D8%B1%D8%B3%D9%84%D9%8A%D9%86%20%D9%88%D8%A7%D9%84%D8%B3%D9%8A%D8%B1%D8%A7%D9%85%D9%8A%D9%83" target="_blank" rel="noopener" class="whatsapp-float-btn" title="تواصل عبر واتساب">
    <svg class="w-7 h-7 fill-current" viewBox="0 0 24 24"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981zm11.387-5.464c-.074-.124-.272-.198-.57-.347-.297-.149-1.758-.868-2.031-.967-.272-.099-.47-.149-.669.149-.198.297-.768.967-.941 1.165-.173.198-.347.223-.644.074-.297-.149-1.255-.462-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.297-.347.446-.521.151-.172.2-.296.3-.495.099-.198.05-.372-.025-.521-.075-.148-.669-1.611-.916-2.206-.242-.579-.487-.501-.669-.51l-.57-.01c-.198 0-.52.074-.792.372s-1.04 1.016-1.04 2.479 1.065 2.876 1.213 3.074c.149.198 2.095 3.2 5.076 4.487.709.306 1.263.489 1.694.626.712.226 1.36.194 1.872.118.571-.085 1.758-.719 2.006-1.413.248-.695.248-1.29.173-1.414z"/></svg>
  </a>

  <!-- Mobile Bottom Navigation Bar -->
  <div class="lg:hidden fixed bottom-0 inset-x-0 bg-surface/95 backdrop-blur-xl border-t border-outline-variant/30 z-40 px-2 py-1 shadow-lg">
    <div class="flex items-center justify-around">
      <a href="index.html" class="flex flex-col items-center py-1 px-3 text-xs text-on-surface-variant hover:text-primary">
        <span class="material-symbols-outlined text-[20px]">home</span>
        <span class="text-[10px] mt-0.5">الرئيسية</span>
      </a>
      <a href="catalog.html" class="flex flex-col items-center py-1 px-3 text-xs text-on-surface-variant hover:text-primary">
        <span class="material-symbols-outlined text-[20px]">category</span>
        <span class="text-[10px] mt-0.5">الكتالوج</span>
      </a>
      <a href="promos.html" class="flex flex-col items-center py-1 px-3 text-xs text-secondary font-bold">
        <span class="material-symbols-outlined text-[20px]">campaign</span>
        <span class="text-[10px] mt-0.5">العروض</span>
      </a>
      <a href="product.html" class="flex flex-col items-center py-1 px-3 text-xs text-on-surface-variant hover:text-primary">
        <span class="material-symbols-outlined text-[20px]">view_in_ar</span>
        <span class="text-[10px] mt-0.5">المنتج</span>
      </a>
      <a href="consultation.html" class="flex flex-col items-center py-1 px-3 text-xs text-on-surface-variant hover:text-primary">
        <span class="material-symbols-outlined text-[20px]">support_agent</span>
        <span class="text-[10px] mt-0.5">استشارة</span>
      </a>
    </div>
  </div>

  <script src="assets/js/main.js"></script>
'''

# New Promotional Models Section to insert on Homepage
promos_homepage_section = '''
<!-- 4.5. MARKETING CAMPAIGNS & PROMOTIONAL MODELS 2025 -->
<section id="campaigns-models" class="w-full bg-surface-container py-space-xl px-gutter md:px-margin-desktop border-y border-outline-variant/30">
  <div class="max-w-[1680px] mx-auto flex flex-col gap-space-lg">
    <div class="flex flex-wrap items-end justify-between gap-space-md">
      <div class="flex flex-col gap-space-xs">
        <div class="inline-flex items-center gap-space-xs text-secondary font-bold text-xs uppercase tracking-widest">
          <span class="material-symbols-outlined text-[18px]">campaign</span>
          <span>نماذج الحملات الإعلانية والبرومو الترويجي لعام 2025</span>
        </div>
        <h2 class="font-headline text-2xl md:text-3xl text-primary font-bold tracking-tight">
          ثلاثة نماذج تسويقية متكاملة لمختلف القنوات والجمهور
        </h2>
        <p class="font-body text-sm text-on-surface-variant max-w-3xl">
          اختر النموذج الأنسب لحملتك: من فيديوهات السوشيال ميديا والريلز، إلى عروض الافتتاح وتخفيضات العرسان الممولة، وحتى تصاميم الفلل والقصور الفاخرة، مع نصيحة ومختبر الموشن والإضاءة القوية.
        </p>
      </div>
      <a href="promos.html" class="bg-primary text-on-primary hover:bg-secondary px-5 py-2.5 rounded font-bold text-xs flex items-center gap-2 transition-all">
        <span>استعراض مركز الحملات الكامل (3 نماذج)</span>
        <span class="material-symbols-outlined text-[16px]">arrow_back</span>
      </a>
    </div>

    <!-- 3 Promotional Models Cards Grid -->
    <div class="grid grid-cols-1 md:grid-cols-3 gap-6 pt-2">
      <!-- Card 1: Social Media -->
      <div class="bg-surface p-6 rounded-xl border border-outline-variant/40 shadow-sm flex flex-col justify-between hover:border-secondary transition-all group">
        <div>
          <div class="flex items-center justify-between mb-3">
            <span class="bg-[#fddeb6] text-[#786041] px-2.5 py-0.5 rounded text-[11px] font-bold">النموذج الأول</span>
            <span class="material-symbols-outlined text-secondary text-[22px]">smart_display</span>
          </div>
          <h3 class="font-bold text-primary text-base mb-2 group-hover:text-secondary transition-colors">
            قوي وجذاب (سوشيال ميديا & فيديوهات قصيرة)
          </h3>
          <p class="text-xs text-on-surface-variant leading-relaxed line-clamp-3 mb-4">
            "بيتك هو عنوان ذوقك.. ولمسات الجمال بتكمل باختيار الصح! 🏡✨ بنوفرلك أحدث صيحات السيراميك والبورسلين اللي بتجمع بين الفخامة والصلابة وسهولة التنظيف..."
          </p>
        </div>
        <div class="pt-4 border-t border-outline-variant/20 flex items-center justify-between">
          <a href="promo-social.html" class="text-xs font-bold text-primary hover:underline">صفحة الحملة ←</a>
          <button data-copy-target="copy-model-1-preview" data-copy-msg="تم نسخ كابشن السوشيال ميديا!" class="text-xs text-secondary hover:text-primary font-bold flex items-center gap-1">
            <span class="material-symbols-outlined text-[14px]">content_copy</span>
            <span>نسخ الكابشن</span>
          </button>
        </div>
        <div id="copy-model-1-preview" class="hidden">بيتك هو عنوان ذوقك.. ولمسات الجمال بتكمل باختيار الصح! 🏡✨ في بورسلانا لارين بنوفرلك أحدث صيحات السيراميك والبورسلين والأدوات الصحية. تنوع مذهل، جودة تضمنلك الاستدامة وسهولة التنظيف، وأسعار تنافسية. زورنا النهاردة واكتشف بنفسك التشكيلة الجديدة! 📍 طريق التخصصي، الرياض 📞 920000000</div>
      </div>

      <!-- Card 2: Offers & Opening -->
      <div class="bg-surface p-6 rounded-xl border-2 border-secondary/40 shadow-md flex flex-col justify-between hover:border-secondary transition-all group relative overflow-hidden">
        <div class="absolute -top-6 -left-6 w-20 h-20 bg-secondary/10 rounded-full blur-xl pointer-events-none"></div>
        <div>
          <div class="flex items-center justify-between mb-3">
            <span class="bg-[#ffdad6] text-[#93000a] px-2.5 py-0.5 rounded text-[11px] font-bold">النموذج الثاني 🔥</span>
            <span class="material-symbols-outlined text-error text-[22px]">local_fire_department</span>
          </div>
          <h3 class="font-bold text-primary text-base mb-2 group-hover:text-secondary transition-colors">
            عروض الافتتاح والتخفيضات (إعلانات ممولة)
          </h3>
          <p class="text-xs text-on-surface-variant leading-relaxed line-clamp-3 mb-4">
            "فرصة لكل عريس وعروسة.. وكل اللي بيجدد بيته! 🛠️🎉 افتتاح وأقوى عروض الموسم في بورسلانا لارين. خصومات حصرية على الفرز الأول وهدايا مع كل تشطيبات الشقق..."
          </p>
        </div>
        <div class="pt-4 border-t border-outline-variant/20 flex items-center justify-between">
          <a href="promo-offers.html" class="text-xs font-bold text-error hover:underline">صفحة العرض الحصري ←</a>
          <button data-copy-target="copy-model-2-preview" data-copy-msg="تم نسخ كابشن العروض والتخفيضات!" class="text-xs text-secondary hover:text-primary font-bold flex items-center gap-1">
            <span class="material-symbols-outlined text-[14px]">content_copy</span>
            <span>نسخ الكابشن</span>
          </button>
        </div>
        <div id="copy-model-2-preview" class="hidden">فرصة لكل عريس وعروسة.. وكل اللي بيجدد بيته! 🛠️🎉 افتتاح أقوى عروض الموسم في معرض بورسلانا لارين للسيراميك والبورسلين. وفرنا لك تشكيلة عالمية بأسعار زمان! 🔥 خصومات حصرية لفترة محدودة على تشكيلات الفرز الأول. 🔥 هدايا ومفاجآت مع كل تشطيبات الشقق الكاملة. 📍 طريق التخصصي، الرياض 📲 920000000</div>
      </div>

      <!-- Card 3: Luxury & Modern Villas -->
      <div class="bg-primary text-on-primary p-6 rounded-xl border border-secondary/30 shadow-lg flex flex-col justify-between hover:border-secondary-fixed transition-all group">
        <div>
          <div class="flex items-center justify-between mb-3">
            <span class="bg-secondary text-white px-2.5 py-0.5 rounded text-[11px] font-bold">النموذج الثالث 💎</span>
            <span class="material-symbols-outlined text-secondary-fixed text-[22px]">diamond</span>
          </div>
          <h3 class="font-bold text-white text-base mb-2 group-hover:text-secondary-fixed transition-colors">
            فخم وراقي (للديكورات الحديثة والفلل)
          </h3>
          <p class="text-xs text-surface-container-high leading-relaxed line-clamp-3 mb-4 font-light">
            "لأن التفاصيل البسيطة هي اللي بتعمل الفرق.. اخترنا لك الأفضل. 💎 تصميمات سيراميك وبورسلين مستوحاة من أحدث اتجاهات الديكور العالمية لتعكس شخصيتك الفريدة..."
          </p>
        </div>
        <div class="pt-4 border-t border-white/10 flex items-center justify-between">
          <a href="promo-luxury.html" class="text-xs font-bold text-secondary-fixed hover:underline">واجهة الفلل الفاخرة ←</a>
          <button data-copy-target="copy-model-3-preview" data-copy-msg="تم نسخ كابشن الفخامة والفلل!" class="text-xs text-secondary-fixed hover:text-white font-bold flex items-center gap-1">
            <span class="material-symbols-outlined text-[14px]">content_copy</span>
            <span>نسخ الكابشن</span>
          </button>
        </div>
        <div id="copy-model-3-preview" class="hidden">لأن التفاصيل البسيطة هي اللي بتعمل الفرق.. اخترنا لك الأفضل. 💎 في بورسلانا لارين بنقدم تصميمات سيراميك وبورسلين مستوحاة من أحدث اتجاهات الديكور العالمية. استمتع بتجربة تسوق فريدة مع فريق استشاريين جاهز لمساعدتك. 📍 طريق التخصصي، الرياض 📞 920000000</div>
      </div>
    </div>

    <!-- Extra Promo Tip Banner (Motion & Strong Lighting) -->
    <div class="bg-surface p-5 rounded-xl border border-secondary/30 flex flex-wrap items-center justify-between gap-4 mt-2">
      <div class="flex items-center gap-3">
        <span class="w-10 h-10 rounded-full bg-secondary-container text-on-secondary-container flex items-center justify-center shrink-0">
          <span class="material-symbols-outlined text-[20px]">lightbulb</span>
        </span>
        <div>
          <span class="text-xs font-bold text-secondary block">نصيحة إضافية لنجاح البرومو:</span>
          <p class="text-xs text-on-surface-variant">"لو هتعمل بيه فيديو، يفضل يكون الفيديو فيه لقطات سريعة وواضحة (Motion) لأفضل أنواع البورسلين والسيراميك داخل المعرض وهي متركبة أو معروضة بإضاءة قوية تبرز لمعتها وجودتها."</p>
        </div>
      </div>
      <a href="promos.html#model-motion-tip" class="bg-secondary text-white hover:bg-secondary-container hover:text-on-secondary-container px-4 py-2 rounded text-xs font-bold transition-colors whitespace-nowrap">
        تجربة مختبر الموشن والإضاءة ←
      </a>
    </div>
  </div>
</section>
'''

# Process index.html
print('Building index.html...')
idx_html = home_src

# Replace <head> custom styling link
idx_html = idx_html.replace('</head>', '<link rel="stylesheet" href="assets/css/custom.css"/></head>')

# Replace Header
idx_html = re.sub(r'<div class="fixed top-0 inset-x-0 z-50 flex flex-col">.*?</header></div>', get_unified_header('home'), idx_html, flags=re.DOTALL)

# Fix links in index.html:
idx_html = idx_html.replace('href="#trending"', 'href="catalog.html"')
idx_html = idx_html.replace('href="#consultation-modal"', 'href="consultation.html"')
idx_html = idx_html.replace('data-path="catalog" href="#"', 'data-path="catalog" href="catalog.html"')
idx_html = idx_html.replace('data-path="product-detail" href="#"', 'data-path="product-detail" href="product.html"')
idx_html = idx_html.replace('data-path="consultation" href="#"', 'data-path="consultation" href="consultation.html"')
idx_html = idx_html.replace('data-path="about" href="#"', 'data-path="about" href="consultation.html"')

# Insert Promotional Models section into Homepage before Section 5 (Tile & Box Calculator Teaser)
idx_html = idx_html.replace('<!-- 5. TILE & BOX CALCULATOR TEASER -->', promos_homepage_section + '\n<!-- 5. TILE & BOX CALCULATOR TEASER -->')

# Replace Footer
idx_html = re.sub(r'<footer class="w-full bg-surface-container-low.*?</footer>', get_unified_footer(), idx_html, flags=re.DOTALL)

# Add title
if '<title>' not in idx_html:
    idx_html = idx_html.replace('<head>', '<head><title>بورسلانا لارين | معرض البورسلين والسيراميك الفاخر</title>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(idx_html)
print('index.html generated successfully!')

# Process catalog.html
print('Building catalog.html...')
cat_html = catalog_src
cat_html = cat_html.replace('</head>', '<link rel="stylesheet" href="assets/css/custom.css"/></head>')
cat_html = re.sub(r'<div class="fixed top-0 inset-x-0 z-50 flex flex-col">.*?</header></div>', get_unified_header('catalog'), cat_html, flags=re.DOTALL)
cat_html = re.sub(r'<footer class="w-full bg-surface-container-low.*?</footer>', get_unified_footer(), cat_html, flags=re.DOTALL)

# Link product cards in catalog to product.html
cat_html = cat_html.replace('href="#" title="استعراض تفاصيل المنتج"', 'href="product.html" title="استعراض تفاصيل المنتج"')
cat_html = cat_html.replace('href="#"', 'href="product.html"')
cat_html = cat_html.replace('طلب عينة مجانية للمنزل', 'طلب عينة للمنزل')

if '<title>' not in cat_html:
    cat_html = cat_html.replace('<head>', '<head><title>كتالوج البورسلين والسيراميك الفاخر 2025 | بورسلانا لارين</title>')

with open('catalog.html', 'w', encoding='utf-8') as f:
    f.write(cat_html)
print('catalog.html generated successfully!')

# Process product.html
print('Building product.html...')
prod_html = product_src
prod_html = prod_html.replace('</head>', '<link rel="stylesheet" href="assets/css/custom.css"/></head>')
prod_html = re.sub(r'<div class="fixed top-0 inset-x-0 z-50 flex flex-col">.*?</header></div>', get_unified_header('product'), prod_html, flags=re.DOTALL)
prod_html = re.sub(r'<footer class="w-full bg-surface-container-low.*?</footer>', get_unified_footer(), prod_html, flags=re.DOTALL)

# Fix breadcrumbs in product.html
prod_html = prod_html.replace('href="#">الرئيسية</a>', 'href="index.html">الرئيسية</a>')
prod_html = prod_html.replace('href="#">البورسلين المعماري</a>', 'href="catalog.html">كتالوج البورسلين</a>')
prod_html = prod_html.replace('href="#">ألواح الحجم الكبير (Mega Slabs)</a>', 'href="catalog.html">ألواح الحجم الكبير</a>')

if '<title>' not in prod_html:
    prod_html = prod_html.replace('<head>', '<head><title>بورسلين كالاكاتا رويال الإيطالي | بورسلانا لارين</title>')

with open('product.html', 'w', encoding='utf-8') as f:
    f.write(prod_html)
print('product.html generated successfully!')

# Process consultation.html
print('Building consultation.html...')
cons_html = consultation_src
cons_html = cons_html.replace('</head>', '<link rel="stylesheet" href="assets/css/custom.css"/></head>')
cons_html = re.sub(r'<div class="fixed top-0 inset-x-0 z-50 flex flex-col">.*?</header></div>', get_unified_header('consultation'), cons_html, flags=re.DOTALL)
cons_html = re.sub(r'<footer class="w-full bg-surface-container-low.*?</footer>', get_unified_footer(), cons_html, flags=re.DOTALL)

cons_html = cons_html.replace('href="#">الرئيسية</a>', 'href="index.html">الرئيسية</a>')

if '<title>' not in cons_html:
    cons_html = cons_html.replace('<head>', '<head><title>حجز استشارة ومعاينة هندسية | بورسلانا لارين</title>')

with open('consultation.html', 'w', encoding='utf-8') as f:
    f.write(cons_html)
print('consultation.html generated successfully!')

print('ALL SITE PAGES BUILT AND CONNECTED!')
