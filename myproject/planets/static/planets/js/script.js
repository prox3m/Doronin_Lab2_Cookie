function setCookie(name, value, days) {
    const maxAge = days * 24 * 60 * 60;
    document.cookie = `${name}=${value}; path=/; max-age=${maxAge}`;
}

const btn = document.querySelector('.theme-toggle');

btn.addEventListener('click', () => {
    document.body.classList.toggle('dark');
    const isDark = document.body.classList.contains('dark');
    setCookie('theme', isDark ? 'dark' : 'light');
})