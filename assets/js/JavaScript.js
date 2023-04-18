renderGalleryView(gallery_data)

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
        div.appendChild(p)
        div.appendChild(img);
        card_container.appendChild(div)
    }
}

function toggleHamburgerMenu() {
    document.getElementById('hamburger-menu').classList.toggle('open')
    document.getElementById('menu-overlay').classList.toggle('open')
}