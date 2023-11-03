window.addEventListener("scroll", onScroll);

function onScroll() {
    const scrollTop = document.documentElement.scrollTop;
    document.getElementById("scrollToTop").style.display = scrollTop > 300 ? "block" : "none";
    if (!title)
        return;
    const scale = Math.max(0.7, 1 - scrollTop / 400);
    title.style.transform = `scale(${scale})`;
}

onScroll();