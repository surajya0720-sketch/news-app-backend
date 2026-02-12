const API_URL = "https://news-app-backend-fd70.onrender.com";

async function loadNews() {
    try {
        const response = await fetch(API_URL);
        const data = await response.json();

        const newsList = document.getElementById("news-list");
        newsList.innerHTML = "";

        data.forEach(news => {
            const card = document.createElement("div");
            card.className = "news-card";

            card.innerHTML = `
                <h3>${news.title}</h3>
                <p>${news.content}</p>
            `;

            newsList.appendChild(card);
        });

    } catch (error) {
        console.error("Error loading news:", error);
    }
}

loadNews();