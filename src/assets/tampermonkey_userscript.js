// ==UserScript==
// @name         toolobjects_functions
// @namespace    http://tampermonkey.net/
// @version      2026-02-06
// @description  functions for image and page saving
// @author       v00d00mag1c
// @match        http*://*/*
// @grant        GM_getValue
// ==/UserScript==

(function() {
    'use strict';

    const DEFAULT_VALUES = {
        'host': 'http://127.0.0.1:22222/api',
        'token': '',
        'images_storage': '',
        'web_pages_storage': '',
        'images_collection': '',
        'web_pages_collection': '',
        'web_pages_webdriver': null,
        'web_bookmarks_collection': null
    }

    const HOST = GM_getValue('host', DEFAULT_VALUES.host);
    const TOKEN = GM_getValue('token', DEFAULT_VALUES.token);
    const IMAGES_STORAGE = GM_getValue('images_storage', DEFAULT_VALUES.images_storage)
    const WEB_PAGES_STORAGE = GM_getValue('web_pages_storage', DEFAULT_VALUES.web_pages_storage)
    const IMAGES_COLLECTION = GM_getValue('images_collection', DEFAULT_VALUES.images_collection)
    const WEB_PAGES_COLLECTION = GM_getValue('web_pages_collection', DEFAULT_VALUES.web_pages_collection)
    const WEB_PAGES_WEBDRIVER = GM_getValue('web_pages_webdriver', DEFAULT_VALUES.web_pages_webdriver)
    const WEB_BOOKMARKS_COLLECTION = GM_getValue('web_bookmarks_collection', DEFAULT_VALUES.web_bookmarks_collection)

    function _api_to_call(args) {
        const url = new URL(HOST)
        const data = new FormData()
        data.set('auth', TOKEN)

        Object.entries(args).forEach(item => {
            if (item[1]) {
                data.set(item[0], item[1])
            }
        })

        return fetch(url.toString(), {
            method: 'post',
            body: data
        })
    }

    document.addEventListener('click', async (e) => {
        if (e.altKey) {
            const target = e.target
            if (target && target.matches('img')) {
                e.preventDefault()
                e.stopPropagation()

                let src = target.src

                await _api_to_call({
                    'i': 'Media.Get',
                    'object': 'Media.Images.Image',
                    'url': [src],
                    'save_to': IMAGES_STORAGE,
                    'link_to': IMAGES_COLLECTION
                })
            }
        }
    })

    document.addEventListener('keyup', async (e) => {
        if (e.ctrlKey && e.altKey && e.code == 'KeyK') {
            await _api_to_call({
                'i': 'Web.Pages.Get',
                'html': document.querySelector('html').innerHTML,
                'save_to': WEB_PAGES_STORAGE,
                'link_to': WEB_PAGES_COLLECTION,
                'set_url': location.href,
                'webdriver': WEB_PAGES_WEBDRIVER
            })
        }

        if (e.ctrlKey && e.altKey && e.code == 'KeyG') {
            const fav = document.querySelector("link[rel*='icon']")
            let fav_url = null
            if (fav) {
                fav_url = fav.href
            }
            await _api_to_call({
                'i': 'Web.Bookmarks.Add',
                'collection': WEB_BOOKMARKS_COLLECTION,
                'url': location.href,
                'title': document.title,
                'favicon': fav_url
            })
        }
    })
})();
