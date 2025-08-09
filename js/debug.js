/* Production no-op debug helpers to prevent 404s */
(function initializeNoOpDebug(){
  try {
    if (typeof window !== 'undefined' && !window.console) {
      window.console = {};
    }
    var methods = ['log','warn','error','info','debug','trace','group','groupEnd'];
    for (var i = 0; i < methods.length; i++) {
      var method = methods[i];
      if (!console[method]) console[method] = function(){ /* no-op */ };
    }
  } catch (e) { /* no-op */ }
})();
