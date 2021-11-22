window.addEventListener('load', (event) => {
    console.log('mchat.js - load');
    if (window.matchMedia("(max-width: 767px)").matches) {
        console.log('mchat.js - isMobile');
        setTimeout(() => {
            let e = {
                chatInput: document.querySelector('.wcInput'),
                wcWindowTitle: document.querySelector('.wcWindowTitle '),
                wcMessages: document.querySelector('.wcMessages'),
                wcUsersCounter: document.querySelector('.wcUsersCounter'),
                wcSubmitButton: document.querySelector('.wcSubmitButton'),
                vimeoVideo: document.querySelector('.livestream_window_viemo_main_custom'),
                footer: document.querySelector('#page-footer'),
                section: document.querySelector('.l-section.height_full'),
                videoContainerLiveStream: document.querySelector('.video-container-livestream'),
                header: document.querySelector('header'),
                body: document.querySelector('body'),
                bodyDiv: document.querySelector('body > div'),
            }

            // removing footer
            e.footer.style.display = 'none';
            // setting body height
            e.body.style.height = '100vh';
            //setting body > div height
            e.bodyDiv.style.height = '100%';
            // adjusting section height and spacing
            e.section.style['min-height'] = 'unset';
            e.section.style['margin-top'] = '50px';
            e.section.style.height = '100%';
            // removing top padding
            e.videoContainerLiveStream.style['padding-top'] = 'unset !important';
            // setting font size on text input field to 16px to prevent Safari auto zoom
            e.chatInput.style['font-size'] = '16px';

            function scrollVideoIntoView() {
                setTimeout(() => {
                    console.log('scrolling into view');
                    e.vimeoVideo.scrollIntoView();
                }, 100);
            }

            function focusActions() {
                console.log('focusActions');
                setTimeout(() => {
                    e.wcMessages.style.height = "0px";
                    e.wcMessages.style.padding = "0px";
                    e.wcUsersCounter.style.height = '0px';
                    e.wcWindowTitle.style.display = 'none';
                    e.header.removeAttribute('hidden');
                    scrollVideoIntoView();
                });
            }

            function blurActions() {
                console.log('blurActions');
                setTimeout(() => {
                    console.log(event);
                    e.wcMessages.style.height = null;
                    e.wcMessages.style.padding = null;
                    e.wcUsersCounter.style.height = null;
                    e.wcWindowTitle.style.display = null;
                    scrollVideoIntoView();
                })
            }

            e.chatInput.addEventListener('focus', (event) => {
                console.log('chatInput - focus');
                focusActions();
            });

            e.chatInput.addEventListener('blur', (event) => {
                console.log('chatInput - blur');
                blurActions();
            });

            // possibly not needed (maybe for ios only)
            e.chatInput.addEventListener('keypress', (event) => {
                console.log('chatInput - keypress', event);
                if (event.keyCode == 13 && !event.shiftKey) {
                    setTimeout(() => {
                        //event.target.blur();
                    })
                }
            })

            let lastResizeInnerHeight = window.innerHeight;
            window.addEventListener("resize", (event) => {
                console.log('window - resize', event);
                // keyboard appeared
                if ( window.innerHeight < lastResizeInnerHeight) {
                    focusActions();
                } else {
                    blurActions();
                }
            });

            console.log('mchat.js - loaded');
        });
    }
});