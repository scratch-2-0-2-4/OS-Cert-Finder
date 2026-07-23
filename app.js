// Application Gestionnaire de Certificats - Vanille JavaScript

// Initialisation au chargement du document
document.addEventListener('DOMContentLoaded', function() {
    initializeApp();
});

function initializeApp() {
    // Initialiser les données de démonstration si vides
    if (!localStorage.getItem('certificates')) {
        const demoCertificates = [
            {
                id: 'LHF-557-vvm',
                nom: 'Scratch.OS X',
                description: '![image markdown](https://via.placeholder.com/300x200?text=Scratch+OS+X)'
            },
            {
                id: 'LHF-558-abc',
                nom: 'Python Avancé',
                description: '![image markdown](https://via.placeholder.com/300x200?text=Python+Avancé)'
            },
            {
                id: 'LHF-559-xyz',
                nom: 'Développement Web Full Stack',
                description: '![image markdown](https://via.placeholder.com/300x200?text=Full+Stack)'
            }
        ];
        localStorage.setItem('certificates', JSON.stringify(demoCertificates));
    }

    // Ajouter la fonctionnalité de recherche si on est sur la page d'accueil
    const searchForm = document.getElementById('searchForm');
    if (searchForm) {
        searchForm.addEventListener('submit', handleSearch);
    }
}

function handleSearch(e) {
    e.preventDefault();

    const searchInput = document.getElementById('searchInput').value.toLowerCase();
    const certificates = JSON.parse(localStorage.getItem('certificates') || '[]');
    const resultsContainer = document.getElementById('results');

    if (!searchInput.trim()) {
        resultsContainer.innerHTML = '<p class="empty-state">Veuillez entrer un terme de recherche.</p>';
        return;
    }

    const results = certificates.filter(cert =>
        cert.id.toLowerCase().includes(searchInput) ||
        cert.nom.toLowerCase().includes(searchInput) ||
        (cert.description && cert.description.toLowerCase().includes(searchInput))
    );

    if (results.length === 0) {
        resultsContainer.innerHTML = '<p class="empty-state">Aucun certificat ne correspond à votre recherche.</p>';
        return;
    }

    resultsContainer.innerHTML = results.map(cert => `
        <div class="certificate-card">
            <h3>${escapeHtml(cert.nom)}</h3>
            <p><strong>ID :</strong> ${escapeHtml(cert.id)}</p>
            <p><strong>Description :</strong> ${renderMarkdown(cert.description || 'Aucune description')}</p>
            <button class="btn btn-primary" onclick="saveCertificateLocally('${escapeHtml(cert.id)}')">;Ajouter à Mes Certificats</button>
        </div>
    `).join('');
}

function saveCertificateLocally(id) {
    const certificates = JSON.parse(localStorage.getItem('certificates') || '[]');
    const certificate = certificates.find(c => c.id === id);

    if (!certificate) {
        alert('Certificat non trouvé.');
        return;
    }

    let userCertificates = JSON.parse(localStorage.getItem('userCertificates') || '[]');

    if (userCertificates.some(c => c.id === id)) {
        alert('Ce certificat est déjà dans vos certificats.');
        return;
    }

    userCertificates.push(certificate);
    localStorage.setItem('userCertificates', JSON.stringify(userCertificates));
    alert('Certificat ajouté à vos certificats !');
}

function escapeHtml(text) {
    if (!text) return '';
    const map = {
        '&': '&amp;',
        '<': '&lt;',
        '>': '&gt;',
        '\"': '&quot;',
        \"'\": '&#039;'
    };
    return text.replace(/[&<>\"']/g, m => map[m]);
}

function renderMarkdown(text) {
    if (!text) return '';
    // Support pour ![alt](url) - images markdown
    return text.replace(/!\[([^\]]*)\]\(([^)]+)\)/g, '<img src="$2" alt="$1" style="max-width: 100%; height: auto; border-radius: 8px; margin: 10px 0;">');
}
