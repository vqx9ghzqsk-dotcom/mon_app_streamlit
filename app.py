<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard Médical - HGR Makala</title>
    <!-- Google Fonts pour un look premium -->
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap" rel="stylesheet">
    <style>
        /* --- DESIGN SYSTEM (SKELETON & AESTHETICS) --- */
        :root {
            --primary: #00796b; 
            --primary-light: #e0f2f1;
            --secondary: #37474f;
            --accent: #26a69a;
            --bg-body: #f0f4f8;
            --bg-card: #ffffff;
            --text-title: #263238;
            --text-body: #455a64;
            --border: #e0e6ed;
            --shadow: 0 10px 30px rgba(0, 0, 0, 0.08);
            --transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        }

        * { box-sizing: border-box; }
        body { font-family: 'Inter', sans-serif; background-color: var(--bg-body); margin: 0; color: var(--text-body); line-height: 1.6; }

        .app-container { max-width: 1250px; margin: 30px auto; background: var(--bg-card); border-radius: 20px; box-shadow: var(--shadow); overflow: hidden; min-height: 90vh; display: flex; flex-direction: column; }

        /* --- HEADER & NAVIGATION --- */
        .app-header { background: #fff; padding: 0 25px; border-bottom: 3px solid var(--primary); display: flex; align-items: center; position: sticky; top: 0; z-index: 1000; box-shadow: 0 4px 10px rgba(0,0,0,0.03); }
        .nav-tabs { display: flex; gap: 10px; padding: 15px 0; flex-grow: 1; }
        .tab { padding: 12px 22px; font-weight: 700; font-size: 12px; text-transform: uppercase; letter-spacing: 0.8px; border: 1px solid var(--border); border-radius: 8px; background: #fafafa; color: var(--text-body); cursor: pointer; transition: var(--transition); display: flex; align-items: center; gap: 10px; }
        .tab:hover { background: var(--primary-light); color: var(--primary); border-color: var(--primary); }
        .tab.active { background: var(--primary); color: #fff; border-color: var(--primary); box-shadow: 0 4px 15px rgba(0, 121, 107, 0.25); }
        
        /* Badges */
        .badge-count { background: rgba(0,0,0,0.1); padding: 2px 8px; border-radius: 20px; font-size: 10px; }
        .tab.active .badge-count { background: rgba(255,255,255,0.2); }

        /* --- CONTENT AREAS --- */
        .tab-content { padding: 40px; display: none; }
        .tab-content.active { display: block; animation: fadeIn 0.5s ease-out; }
        @keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }

        /* --- UI COMPONENTS (SKELETON ELEMENTS) --- */
        .section-header { margin: 30px 0 20px; padding: 15px 25px; background: var(--primary-light); color: var(--primary-dark); font-weight: 800; border-left: 8px solid var(--primary); border-radius: 4px 12px 12px 4px; text-transform: uppercase; font-size: 14px; }
        
        .grid-3 { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px; margin-bottom: 25px; }
        .input-group { display: flex; flex-direction: column; gap: 8px; }
        label { font-size: 13px; font-weight: 800; color: var(--secondary); display: flex; align-items: center; gap: 5px; }
        input, select, textarea { padding: 14px; border: 2px solid #edf2f7; border-radius: 10px; font-size: 15px; width: 100%; transition: var(--transition); }
        input:focus, select:focus { border-color: var(--accent); outline: none; box-shadow: 0 0 0 4px rgba(38, 166, 154, 0.1); }

        /* Checkbox Box Grid */
        .checkbox-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px; padding: 20px; background: #fcfcfc; border: 2px dashed var(--border); border-radius: 12px; }
        .check-pill { display: flex; align-items: center; gap: 12px; padding: 12px; background: #fff; border: 1px solid var(--border); border-radius: 8px; cursor: pointer; transition: 0.2s; font-size: 14px; font-weight: 600; }
        .check-pill:hover { border-color: var(--primary); background: var(--primary-light); }
        .check-pill input { width: 18px; height: 18px; margin: 0; accent-color: var(--primary); }

        /* Buttons */
        .btn-primary { background: var(--primary); color: #fff; padding: 18px 30px; border: none; border-radius: 12px; font-weight: 800; cursor: pointer; width: 100%; font-size: 16px; text-transform: uppercase; margin-top: 30px; transition: var(--transition); box-shadow: 0 8px 15px rgba(0, 121, 107, 0.2); }
        .btn-primary:hover { transform: translateY(-3px); box-shadow: 0 12px 25px rgba(0, 121, 107, 0.3); }

        /* Tables & Matrix */
        .matrix-container { overflow-x: auto; border-radius: 12px; border: 1px solid var(--border); }
        table { width: 100%; border-collapse: collapse; min-width: 800px; }
        th { background: #f8fafc; padding: 18px; text-align: left; font-size: 12px; font-weight: 800; color: var(--secondary); border-bottom: 2px solid var(--border); }
        td { padding: 18px; border-bottom: 1px solid var(--border); font-size: 14px; }

        /* Stats Cards */
        .stat-card { background: #fff; border: 1px solid var(--border); padding: 25px; border-radius: 15px; }
        .stat-value { font-size: 32px; font-weight: 800; color: var(--primary); }
        .stat-label { font-size: 12px; color: var(--text-body); font-weight: 700; margin-top: 5px; }
    </style>
</head>
<body>

<div class="app-container">
    <header class="app-header">
        <nav class="nav-tabs">
            <button class="tab active" onclick="switchTab(1)">1. Collecte 📋 <span class="badge-count" id="badge-1">150</span></button>
            <button class="tab" onclick="switchTab(2)">2. Matrice de Dépouillement 📊</button>
            <button class="tab" onclick="switchTab(3)">3. Résultats & Analyse 📈</button>
            <button class="tab" onclick="switchTab(4)">4. Synthèse finale 📄</button>
        </nav>
        <div style="font-size: 10px; font-weight: 800; color: #999; text-transform: uppercase;">MAKALA-TB-2024</div>
    </header>

    <!-- TAB 1: COLLECTE (FICHE TB) -->
    <div id="content-1" class="tab-content active">
        <div style="text-align:center; margin-bottom: 40px;">
            <h2 style="margin:0; font-weight:800; color:var(--text-title);">FICHE D'ENQUÊTE CLINIQUE</h2>
            <p style="margin:5px 0 0; color:var(--text-body); font-weight:600; font-size:14px;">Profil de la tuberculose pulmonaire - HGR Makala</p>
        </div>

        <form id="collecteForm">
            <div class="section-header">I. IDENTIFICATION DU DOSSIER</div>
            <div class="grid-3">
                <div class="input-group">
                    <label>Numéro de fiche</label>
                    <input type="text" placeholder="Ex: F-MAK-001" id="num-fiche">
                </div>
                <div class="input-group">
                    <label>Numéro du dossier</label>
                    <input type="text" placeholder="Numéro hospitalier..." id="num-dossier">
                </div>
                <div class="input-group">
                    <label>Année d'admission</label>
                    <select id="annee">
                        <option value="2023">2023</option>
                        <option value="2024" selected>2024</option>
                    </select>
                </div>
            </div>

            <div class="section-header">III. ANTÉCÉDENTS MÉDICAUX</div>
            <div class="grid-3">
                <div class="input-group">
                    <label>Antécédent de tuberculose</label>
                    <select id="ant-tb">
                        <option value="non">Non</option>
                        <option value="oui">Oui</option>
                    </select>
                </div>
                <div class="input-group">
                    <label>Statut VIH</label>
                    <select id="stat-vih">
                        <option value="neg">Négatif</option>
                        <option value="pos">Positif</option>
                        <option value="inc">Inconnu</option>
                    </select>
                </div>
                <div class="input-group">
                    <label>Diabète</label>
                    <select id="diabetes">
                        <option value="non">Non</option>
                        <option value="oui">Oui</option>
                    </select>
                </div>
            </div>

            <div class="section-header">IV. DONNÉES CLINIQUES & SYMPTÔMES</div>
            <div class="input-group" style="margin-bottom: 25px;">
                <label>Motif d'admission</label>
                <textarea rows="2" placeholder="Saisir ici le motif principal..."></textarea>
            </div>

            <label style="margin-bottom: 12px; display: block;">Symptômes présents :</label>
            <div class="checkbox-grid">
                <label class="check-pill"><input type="checkbox"> Toux</label>
                <label class="check-pill"><input type="checkbox"> Toux ≥ 2 semaines</label>
                <label class="check-pill"><input type="checkbox"> Hémoptysie</label>
                <label class="check-pill"><input type="checkbox"> Fièvre</label>
                <label class="check-pill"><input type="checkbox"> Sueurs nocturnes</label>
                <label class="check-pill"><input type="checkbox"> Amaigrissement</label>
                <label class="check-pill"><input type="checkbox"> Douleur thoracique</label>
                <label class="check-pill"><input type="checkbox"> Dyspnée</label>
            </div>

            <div class="grid-3" style="margin-top: 30px;">
                <div class="input-group">
                    <label>Durée symptômes (semaines)</label>
                    <input type="number" placeholder="Ex: 4">
                </div>
                <div class="input-group">
                    <label>État général</label>
                    <select>
                        <option value="bon">Bon</option>
                        <option value="altere">Altéré</option>
                    </select>
                </div>
            </div>

            <div class="section-header">VIII. ÉVOLUTION CLINIQUE</div>
            <div class="input-group" style="max-width: 400px;">
                <label>Issue (Résultat final)</label>
                <select>
                    <option value="" disabled selected>Choisir l'issue...</option>
                    <option>Guérison</option>
                    <option>Amélioration</option>
                    <option>Transfert</option>
                    <option>Décès</option>
                    <option>Perdu de vue</option>
                </select>
            </div>

            <button type="button" class="btn-primary">📤 Enregistrer dans la matrice</button>
        </form>
    </div>

    <!-- TAB 2: MATRICE -->
    <div id="content-2" class="tab-content">
        <h2 style="font-weight: 800;">BASE DE DONNÉES EN LIGNE (N=150)</h2>
        <div class="matrix-container">
            <table>
                <thead>
                    <tr>
                        <th>N° FICHE</th><th>DOSSIER</th><th>ANT_TB</th><th>VIH</th><th>DIABÈTE</th><th>ISSUE</th><th>ACTION</th>
                    </tr>
                </thead>
                <tbody id="matrixBody">
                    <!-- Données simulées pour le squelette -->
                    <tr><td>F-MAK-001</td><td>DOS-104</td><td>Non</td><td>Négatif</td><td>Non</td><td>Guérison</td><td><button style="font-size:10px; padding:5px 10px; border-radius:5px; border:1px solid #ccc; cursor:pointer;">Éditer</button></td></tr>
                    <tr><td>F-MAK-002</td><td>DOS-208</td><td>Oui</td><td>Positif</td><td>Non</td><td>Décès</td><td><button style="font-size:10px; padding:5px 10px; border-radius:5px; border:1px solid #ccc; cursor:pointer;">Éditer</button></td></tr>
                </tbody>
            </table>
        </div>
    </div>

    <!-- TAB 3: RÉSULTATS -->
    <div id="content-3" class="tab-content">
        <h2 style="font-weight: 800;">TABLEAUX ANALYTIQUES GÉNÉRÉS</h2>
        <div class="grid-3">
            <div class="stat-card">
                <div class="stat-value">28%</div>
                <div class="stat-label">Taux de co-infection TB-VIH</div>
            </div>
            <div class="stat-card">
                <div class="stat-value">14.2%</div>
                <div class="stat-label">Taux de Létalité Global (CFR)</div>
            </div>
            <div class="stat-card">
                <div class="stat-value">4.5 sem.</div>
                <div class="stat-label">Durée moyenne des symptômes</div>
            </div>
        </div>
        
        <div class="section-header">Visualisation des tendances cliniques</div>
        <div style="height: 300px; background: #fafafa; border-radius: 12px; border: 2px dashed #eee; display:flex; align-items:center; justify-content:center; color:#999; font-weight:700;">
            [ Zone Graphiques (Symptômes vs VIH) ]
        </div>
    </div>

    <!-- TAB 4: SYNTHÈSE -->
    <div id="content-4" class="tab-content">
        <h2 style="font-weight: 800;">RAPPORT FINAL DE SYNTHÈSE</h2>
        <div style="background: #fff; border: 1px solid var(--border); padding: 30px; border-radius: 15px; border-left: 10px solid var(--primary);">
            <p><strong>Conclusion :</strong> L'analyse des 150 dossiers d'admission suggère une corrélation forte entre le statut sérologique VIH et l'issue fatale (Décès). La triade Toux - Fièvre - Amaigrissement reste le profil symptomatique dominant...</p>
        </div>
        <button class="btn-primary" style="background: var(--secondary); max-width: 300px;">📥 Télécharger le rapport (.CSV)</button>
    </div>
</div>

<script>
    function switchTab(idx) {
        document.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));
        document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
        
        document.getElementById('content-' + idx).classList.add('active');
        document.querySelectorAll('.tab')[idx-1].classList.add('active');
        window.scrollTo(0,0);
    }
</script>

</body>
</html>
