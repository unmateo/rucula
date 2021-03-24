function refresh() {
    const token = localStorage.getItem('token');
    const currentLocation = window.location.href;
    console.debug(currentLocation);
    if (!currentLocation.includes('?token=')) {
        const url = `${currentLocation}?token=${token}`;
        console.debug(url);
        window.location.replace(url);
    }
    console.info('Already inside.');
}
