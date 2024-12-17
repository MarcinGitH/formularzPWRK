// Funkcja do wyświetlania okienka z danymi w miejscu kliknięcia
document.querySelectorAll('.item-row').forEach(function (row) {
    row.addEventListener('click', function (event) {
        // Zatrzymujemy propagację kliknięcia na wiersz, jeśli kliknięto ikonę kopiowania
        if (event.target.classList.contains('copy-btn')) {
            return; // Zatrzymujemy propagację
        }

        // Pobieramy dane z atrybutów wiersza
        var id = this.getAttribute('data-id');
        var description_1 = this.getAttribute('data-description_1');
        var status = this.getAttribute('data-status');
        var type_of_employee = this.getAttribute('data-type_of_employee');
        var type_of_tool = this.getAttribute('data-type_of_tool');
        var reason = this.getAttribute('data-reason');
        var producer = this.getAttribute('data-producer');
        var supplier = this.getAttribute('data-supplier');
        var manage_employee = this.getAttribute('data-manage_employee');
        var drawings_2d = this.getAttribute('data-drawings_2d');
        var drawings_3d = this.getAttribute('data-drawings_3d');
        var screen_catalog = this.getAttribute('data-screen_catalog');
        var comments = this.getAttribute('data-comments');
        var change_date = this.getAttribute('data-change_date');
        var entry_date = this.getAttribute('data-entry_date');

        // Ustawiamy dane w okienku



        document.getElementById('popup-id').textContent = id;
        document.getElementById('popup-description_1').textContent = description_1;
        document.getElementById('popup-description_1').title = description_1;
        document.getElementById('popup-status').textContent = status;
        document.getElementById('popup-type_of_employee').textContent = type_of_employee;
        document.getElementById('popup-type_of_tool').textContent = type_of_tool;
        document.getElementById('popup-reason').textContent = reason;
        document.getElementById('popup-producer').textContent = producer;
        document.getElementById('popup-supplier').textContent = supplier;
        document.getElementById('popup-manage_employee').textContent = manage_employee;
        document.getElementById('popup-drawings_2d').textContent = drawings_2d;
        document.getElementById('popup-drawings_3d').href = "{% url 'download-handling' " + drawings_3d + " %}";
        document.getElementById('popup-screen_catalog').textContent = screen_catalog;
        document.getElementById('popup-comments').textContent = ifNoneReturnEmpty(comments);
        document.getElementById('popup-change_date').textContent = change_date;
        document.getElementById('popup-entry_date').textContent = entry_date;

        // Wyświetlamy okienko w miejscu kliknięcia
        var popup = document.getElementById('data-popup');

        // Obliczamy pozycję popupu względem kliknięcia
        var posX = event.clientX + window.scrollX;  // Uwzględniamy przewinięcie strony
        var posY = event.clientY + window.scrollY;  // Uwzględniamy przewinięcie strony

        // Sprawdzamy, czy popup nie wychodzi poza ekran
        popup.style.display = 'block';  // Pokazujemy popup
        var popupWidth = popup.offsetWidth;
        var popupHeight = popup.offsetHeight;

        if (posX + popupWidth > window.innerWidth) {
            posX = window.innerWidth - popupWidth - 30;
        }

        if (posY + popupHeight > window.innerHeight) {
            posY = window.innerHeight - popupHeight - 30;
        }

        //nadpisuje te 2 linijki, zeby popup pojawil sie na srodku ekranu
        //popup.style.top = posY+30 + 'px';
        //popup.style.left = posX + 'px';
        popup.style.top = (window.innerHeight - popupHeight) / 2 + "px";
        popup.style.left = (window.innerWidth - popupWidth) / 2 + "px";

        // Zatrzymujemy propagację, aby zapobiec wywołaniu innych zdarzeń kliknięcia
        event.stopPropagation();
    });
});