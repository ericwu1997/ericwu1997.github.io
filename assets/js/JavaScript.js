renderGalleryView(gallery_data)

document.addEventListener("scroll", (event) => {
    document.getElementById('menu-overlay').classList.remove('open');
    document.getElementById('hamburger-menu').classList.remove('open')
});

function scrollToTop() {
    scrollToSmoothly(document.getElementById('header').offsetTop, 200)
}

function scrollToBottom() {
    scrollToSmoothly(document.getElementById('footer').offsetTop, 200)
}

function scrollToSmoothly(pos, time) {
    var currentPos = window.pageYOffset;
    var start = null;
    if(time == null) time = 500;
    pos = +pos, time = +time;
    window.requestAnimationFrame(function step(currentTime) {
        start = !start ? currentTime : start;
        var progress = currentTime - start;
        if (currentPos < pos) {
            window.scrollTo(0, ((pos - currentPos) * progress / time) + currentPos);
        } else {
            window.scrollTo(0, currentPos - ((currentPos - pos) * progress / time));
        }
        if (progress < time) {
            window.requestAnimationFrame(step);
        } else {
            window.scrollTo(0, pos);
        }
    });
}

function renderGalleryView(list) {
    list.sort((a, b) => {
        let a_num = parseInt(a.product.name.match(/\d{1,3}/));
        let b_num = parseInt(b.product.name.match(/\d{1,3}/));
        if (a_num < b_num) return -1;
        if (a_num > b_num) return 1;
        return 0;
    })

    let card_container = document.getElementById("card-container");
    let size = list.length;
    for (let i = 0; i < size; i++) {
        let div = document.createElement('div');
        let img = document.createElement('img');
        let p = document.createElement('p');
        p.innerHTML = list[i].product.name;
        img.setAttribute("src", list[i].product.img.src);
        div.classList.add("card");
        div.appendChild(p)
        div.appendChild(img);
        card_container.appendChild(div)
    }
}

function toggleHamburgerMenu() {
    document.getElementById('hamburger-menu').classList.toggle('open')
    document.getElementById('menu-overlay').classList.toggle('open')
}