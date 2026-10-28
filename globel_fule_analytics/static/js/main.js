/**
 * Global Fuel Prices and Taxation Trends - Interactive Scripts
 * Handles Tableau viz embedding, loading states, fallback handling, and UI helpers
 */

document.addEventListener('DOMContentLoaded', function () {
  // 1. Initialize Bootstrap Tooltips if available
  const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
  tooltipTriggerList.map(function (tooltipTriggerEl) {
    return new bootstrap.Tooltip(tooltipTriggerEl);
  });

  // 2. Tableau Iframe Loading & Fallback Management
  const tableauFrame = document.getElementById('tableauEmbedFrame');
  const loadingIndicator = document.getElementById('tableauLoadingIndicator');
  const fallbackNotice = document.getElementById('tableauFallbackNotice');

  if (tableauFrame && loadingIndicator) {
    let frameLoaded = false;

    // When the iframe reports onload
    tableauFrame.addEventListener('load', function () {
      frameLoaded = true;
      loadingIndicator.style.opacity = '0';
      setTimeout(function () {
        loadingIndicator.style.display = 'none';
      }, 400);
    });

    // Timeout safety fallback: If Tableau takes > 7 seconds (offline, slow connection, or adblocker)
    setTimeout(function () {
      if (!frameLoaded) {
        if (loadingIndicator) {
          loadingIndicator.style.display = 'none';
        }
        if (fallbackNotice) {
          fallbackNotice.classList.remove('d-none');
        }
      }
    }, 7000);
  }

  // 3. Fullscreen Toggle for Tableau Visualizations
  const fullscreenBtn = document.getElementById('btnToggleFullscreen');
  const vizWrapper = document.getElementById('tableauWrapper');

  if (fullscreenBtn && vizWrapper) {
    fullscreenBtn.addEventListener('click', function () {
      if (!document.fullscreenElement) {
        if (vizWrapper.requestFullscreen) {
          vizWrapper.requestFullscreen();
        } else if (vizWrapper.webkitRequestFullscreen) {
          vizWrapper.webkitRequestFullscreen();
        } else if (vizWrapper.msRequestFullscreen) {
          vizWrapper.msRequestFullscreen();
        }
        fullscreenBtn.innerHTML = '<i class="bi bi-fullscreen-exit me-1"></i> Exit Fullscreen';
      } else {
        if (document.exitFullscreen) {
          document.exitFullscreen();
        }
        fullscreenBtn.innerHTML = '<i class="bi bi-arrows-fullscreen me-1"></i> Fullscreen';
      }
    });

    document.addEventListener('fullscreenchange', function () {
      if (!document.fullscreenElement) {
        fullscreenBtn.innerHTML = '<i class="bi bi-arrows-fullscreen me-1"></i> Fullscreen';
      }
    });
  }

  // 4. Copy Dashboard Link Helper
  const copyBtn = document.getElementById('btnCopyDashboardLink');
  if (copyBtn) {
    copyBtn.addEventListener('click', function () {
      const urlToCopy = copyBtn.getAttribute('data-url') || window.location.href;
      navigator.clipboard.writeText(urlToCopy).then(function () {
        const originalText = copyBtn.innerHTML;
        copyBtn.innerHTML = '<i class="bi bi-check2 me-1"></i> Copied!';
        copyBtn.classList.remove('btn-outline-light');
        copyBtn.classList.add('btn-success');
        setTimeout(function () {
          copyBtn.innerHTML = originalText;
          copyBtn.classList.remove('btn-success');
          copyBtn.classList.add('btn-outline-light');
        }, 2000);
      }).catch(function (err) {
        console.error('Could not copy link: ', err);
      });
    });
  }

  // 5. Reload Visual Helper
  const reloadBtn = document.getElementById('btnReloadViz');
  if (reloadBtn && tableauFrame) {
    reloadBtn.addEventListener('click', function () {
      if (loadingIndicator) {
        loadingIndicator.style.display = 'flex';
        loadingIndicator.style.opacity = '1';
      }
      tableauFrame.src = tableauFrame.src;
    });
  }
});

