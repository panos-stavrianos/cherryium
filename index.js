import 'jquery'
import './app/src/js/jquery_import'
import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.css' // Import precompiled Bootstrap css
import '@fortawesome/fontawesome-free/css/all.css'

import 'inputmask/dist/jquery.inputmask.min'
import 'popper.js'
import 'chartjs'
import 'perfect-scrollbar'
import 'flag-icon-css/css/flag-icon.min.css'
import 'particles.js'
import './app/src/js/bootstrap-notify'
import './app/src/css/404.css'
import './app/src/css/now-ui-dashboard.css'
import './app/src/js/now-ui-dashboard'
import UrlPattern from "url-pattern";
import './app/src/js/custom'
import './app/src/js/bs_sidebar'
import './app/src/js/help'

String.prototype.match_url = function (url) {
    const pattern = new UrlPattern(this, {segmentNameCharset: 'a-zA-Z0-9_-'});
    return pattern.match(url) !== null;
};


const pathname = window.location.pathname;
switch (true) {
    case '/'.match_url(pathname):
        import('./app/src/js/dashboard').then(page => page.render());
        break;
    case '/user/edit_user_profile'.match_url(pathname):
        console.log('home');
        // import('./app/src/js/custom').then(page => page.render());
        break;
    case '/user/sign-in'.match_url(pathname):
    case '/user/register'.match_url(pathname):
    case '/user/forgot-password'.match_url(pathname):
    case '/user/reset-password/:token'.match_url(pathname):
        import('./app/src/js/login').then(page => page.render());
        break;
    case '/customers'.match_url(pathname):
        import('./app/src/js/customers').then(page => page.render());
        break;
    case '/products'.match_url(pathname):
        import('./app/src/js/products').then(page => page.render());
        break;
    case '/services'.match_url(pathname):
        import('./app/src/js/services').then(page => page.render());
        break;
    case '/expenses'.match_url(pathname):
        import('./app/src/js/expenses').then(page => page.render());
        break;
    case '/partners'.match_url(pathname):
        import('./app/src/js/partners').then(page => page.render());
        break;
    case '/customer/:id'.match_url(pathname):
        import('./app/src/js/customer').then(page => page.render());
        break;
    case '/product/:id'.match_url(pathname):
        import('./app/src/js/product').then(page => page.render());
        break;
    case '/service/:id'.match_url(pathname):
        import('./app/src/js/service').then(page => page.render());
        break;
    case '/expense/:id'.match_url(pathname):
        import('./app/src/js/expense').then(page => page.render());
        break;
    case '/partner/:id'.match_url(pathname):
        import('./app/src/js/partner').then(page => page.render());
        break;
    default:
        import('./app/src/js/login').then(page => page.render());
}
