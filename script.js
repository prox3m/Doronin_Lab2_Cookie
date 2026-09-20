const btn = document.querySelector('.theme-toggle');

if (localStorage.getItem('theme') === 'dark') {
    document.body.classList.add('dark');
}

btn.addEventListener('click', () => {
    document.body.classList.toggle('dark');
    const isDark = document.body.classList.contains('dark');
    localStorage.setItem('theme', isDark ? 'dark' : 'light');
})