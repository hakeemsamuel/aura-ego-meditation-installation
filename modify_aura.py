import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add CSS
css_to_add = """
        /* MODE SELECTION UI */
        #mode-select-ui {
            position: absolute;
            top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(0, 0, 0, 0.8);
            backdrop-filter: blur(10px);
            z-index: 1000;
            display: none;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }
        .ms-title {
            font-size: 28px;
            font-weight: 600;
            margin-bottom: 8px;
        }
        .ms-sub {
            font-size: 16px;
            font-weight: 400;
            opacity: 0.8;
            margin-bottom: 40px;
        }
        .ms-cards {
            display: flex;
            gap: 30px;
        }
        .ms-card {
            width: 320px;
            padding: 30px;
            border-radius: 16px;
            cursor: pointer;
            position: relative;
        }
        .ms-card:hover {
            border-color: #FF5D8F;
            box-shadow: 0 0 20px rgba(255, 93, 143, 0.4);
        }
        .ms-card .badge {
            position: absolute;
            top: -12px;
            right: 20px;
            background: #FF5D8F;
            color: #fff;
            padding: 4px 12px;
            border-radius: 12px;
            font-size: 12px;
            font-weight: 600;
        }
        .ms-card .icon {
            font-size: 40px;
            margin-bottom: 20px;
        }
        .ms-card-title {
            font-size: 20px;
            font-weight: 600;
            margin-bottom: 12px;
        }
        .ms-card-desc {
            font-size: 14px;
            opacity: 0.9;
            line-height: 1.5;
            margin-bottom: 20px;
        }
        .ms-card-dur {
            font-size: 12px;
            opacity: 0.6;
        }
        .ms-bot {
            margin-top: 40px;
            font-size: 14px;
            opacity: 0.6;
        }
"""
content = content.replace("</style>", css_to_add + "\n    </style>")

# 2. Add UI HTML
html_to_add = """
    <div id="mode-select-ui">
        <div class="ms-title">Choose Your Experience</div>
        <div class="ms-sub">Select how you'd like to practice</div>
        <div class="ms-cards">
            <div class="glm ms-card" onclick="selectMode('MEDITATION_STRETCH')">
                <div class="badge">Recommended</div>
                <div class="icon">🧍</div>
                <div class="ms-card-title">Meditation & Stretch</div>
                <div class="ms-card-desc">Gentle stretches while standing. Perfect for beginners or exhibition viewing.</div>
                <div class="ms-card-dur">10 minutes</div>
            </div>
            <div class="glm ms-card" onclick="selectMode('GUIDED_YOGA')">
                <div class="icon">🧘</div>
                <div class="ms-card-title">Guided Yoga Flow</div>
                <div class="ms-card-desc">Full yoga sequence with floor poses. For those comfortable with yoga practice.</div>
                <div class="ms-card-dur">10 minutes</div>
            </div>
        </div>
        <div class="ms-bot">Press 'M' anytime to return to menu</div>
    </div>
"""
content = content.replace('<div id="ldr">✨ Illuminating Space...</div>', '<div id="ldr">✨ Illuminating Space...</div>\n' + html_to_add)

# 3. Modify Constants (PHS, PSS, GDS)
const_def = """
        let MAX_T = 640;
        const MODES = { A: 'MEDITATION_STRETCH', B: 'GUIDED_YOGA' };
        let currentMode = null;

        const PHS_A = [
            { id: 1, st: 0, nd: 120, nm: 'GROUNDING', b1: '#2D1525', b2: '#4A2A44', c: ['#E6B3FF', '#FFB3BA'], br: '#E6B3FF', rv: 0.4 },
            { id: 2, st: 120, nd: 300, nm: 'GENTLE MOVEMENT', b1: '#4A2A44', b2: '#6B3D66', c: ['#FFB3BA', '#FFDFBA'], br: '#FFDFBA', rv: 0.5 },
            { id: 3, st: 300, nd: 420, nm: 'OPENING', b1: '#6B3D66', b2: '#A3687F', c: ['#FFDFBA', '#FFFFBA'], br: '#FFFFBA', rv: 0.7 },
            { id: 4, st: 420, nd: 540, nm: 'STILLNESS', b1: '#A3687F', b2: '#D6899E', c: ['#E6B3FF', '#FFB3BA'], br: '#FFB3BA', rv: 0.9 },
            { id: 5, st: 540, nd: 600, nm: 'INTEGRATION', b1: '#D6899E', b2: '#2D1525', c: ['#B3C6FF', '#E6B3FF'], br: '#B3C6FF', rv: 0.5 }
        ];
        const PHS_B = [
            { id: 1, st: 0, nd: 120, nm: 'GROUNDING', b1: '#2D1040', b2: '#4A1958', c: ['#FF10F0', '#FF006E'], br: '#4A1958', rv: 0.3 },
            { id: 2, st: 120, nd: 300, nm: 'FLOW', b1: '#4A1958', b2: '#8D3087', c: ['#F72585', '#FF5D8F'], br: '#F72585', rv: 0.6 },
            { id: 3, st: 300, nd: 420, nm: 'EXPANSION', b1: '#8D3087', b2: '#C4556F', c: ['#FF5D8F', '#FFB627', '#FF8500'], br: '#FF8500', rv: 0.8 },
            { id: 4, st: 420, nd: 540, nm: 'PEAK', b1: '#C4556F', b2: '#FFA040', c: ['#FF10F0', '#F72585', '#FF5D8F', '#FFB627', '#FF8500', '#FFD700'], br: '#FFD700', rv: 1.0 },
            { id: 5, st: 540, nd: 640, nm: 'INTEGRATION', b1: '#FFA040', b2: '#2D1040', c: ['#FFB627', '#E0B0FF', '#FF10F0'], br: '#E0B0FF', rv: 0.4 }
        ];
        let PHS = PHS_B;

        const PSS_A = [
            { n: "Mountain Pose", st: 5, nd: 35, ph: 1, t: "STANDING" },
            { n: "Standing Arm Raises", st: 35, nd: 65, ph: 1, t: "STANDING_UP" },
            { n: "Standing Side Stretch", st: 65, nd: 95, ph: 1, t: "STANDING" },
            { n: "Partial Forward Fold", st: 95, nd: 125, ph: 1, t: "STANDING_P_FOLD" },
            { n: "Standing Twist", st: 125, nd: 170, ph: 2, t: "STANDING" },
            { n: "Standing Hip Circles", st: 170, nd: 215, ph: 2, t: "STANDING" },
            { n: "Standing Arm Circles", st: 215, nd: 260, ph: 2, t: "STANDING" },
            { n: "Standing Tree Prep", st: 260, nd: 305, ph: 2, t: "STANDING" },
            { n: "Standing Chest Opener", st: 305, nd: 350, ph: 3, t: "STANDING_WIDE" },
            { n: "Standing Side Reach", st: 350, nd: 395, ph: 3, t: "STANDING_REACH" },
            { n: "Standing Heart Opener", st: 395, nd: 425, ph: 3, t: "STANDING" },
            { n: "Standing Meditation", st: 425, nd: 515, ph: 4, t: "STANDING_MED" },
            { n: "Gentle Standing Sway", st: 515, nd: 545, ph: 5, t: "STANDING" },
            { n: "Standing Gratitude", st: 545, nd: 585, ph: 5, t: "STANDING_MED" }
        ];
        const PSS_B = [
            { n: "Mountain Pose", st: 5, nd: 35, ph: 1, t: "STANDING" }, { n: "Raised Hands", st: 35, nd: 65, ph: 1, t: "STANDING_UP" },
            { n: "Side Stretch", st: 65, nd: 95, ph: 1, t: "STANDING" }, { n: "Forward Fold", st: 95, nd: 125, ph: 1, t: "STANDING_FOLD" },
            { n: "Cat-Cow", st: 125, nd: 185, ph: 2, t: "FLOOR" }, { n: "Downward Dog", st: 190, nd: 235, ph: 2, t: "FLOOR_INV" },
            { n: "Child's Pose", st: 240, nd: 285, ph: 2, t: "FLOOR_R" }, { n: "Seated Twist", st: 290, nd: 320, ph: 2, t: "SEATED" },
            { n: "Warrior I", st: 325, nd: 370, ph: 3, t: "STANDING_A_U" }, { n: "Warrior II", st: 375, nd: 420, ph: 3, t: "STANDING_A_S" },
            { n: "Triangle", st: 425, nd: 455, ph: 3, t: "STANDING" }, { n: "Seated Meditation", st: 455, nd: 545, ph: 4, t: "SEATED_MED" },
            { n: "Supine Twist", st: 545, nd: 590, ph: 5, t: "LYING" }, { n: "Savasana", st: 595, nd: 640, ph: 5, t: "LYING_R" }
        ];
        let PSS = PSS_B;

        const GDS_A = [
            { t: 5, x: "Welcome. Notice your feet on the ground.", a: "ma_01" },
            { t: 35, x: "Breathe in, gently raise your arms.", a: "ma_02" },
            { t: 65, x: "Feel the space as you stretch to the side.", a: "ma_03" },
            { t: 95, x: "Soft knees. Gently fold forward.", a: "ma_04" },
            { t: 125, x: "Rise. Rotate and twist softly.", a: "ma_05" },
            { t: 170, x: "Circle the hips. Find your center.", a: "ma_06" },
            { t: 215, x: "Let your arms circle like natural breath.", a: "ma_07" },
            { t: 260, x: "Shift your weight. Prepare for balance.", a: "ma_08" },
            { t: 305, x: "Open your chest and heart.", a: "ma_09" },
            { t: 350, x: "Reach softly to the sides.", a: "ma_10" },
            { t: 395, x: "Heart opener. Breathe fully.", a: "ma_11" },
            { t: 425, x: "Standing meditation. Be present.", a: "ma_12" },
            { t: 470, x: "Notice the stillness within.", a: "ma_13" },
            { t: 515, x: "Gentle sway, like a tree in the wind.", a: "ma_14" },
            { t: 545, x: "Gratitude. Hands to the heart.", a: "ma_15" },
            { t: 575, x: "Rest and integrate.", a: "ma_16" }
        ];
        const GDS_B = [
            { t: 5, x: "Welcome. Let's begin with Mountain Pose.", a: "m_01" }, { t: 15, x: "Stand tall.", a: "m_02" }, { t: 35, x: "Raise arms overhead.", a: "r_01" },
            { t: 65, x: "Gently bend right.", a: "s_01" }, { t: 95, x: "Fold forward.", a: "f_01" }, { t: 125, x: "Hands and knees. Cat-Cow.", a: "c_01" },
            { t: 190, x: "Downward Dog.", a: "d_01" }, { t: 240, x: "Child's Pose.", a: "ch_01" }, { t: 290, x: "Seated twist right.", a: "tw_01" },
            { t: 325, x: "Rise up. Warrior I.", a: "w1_01" }, { t: 375, x: "Warrior II.", a: "w2_01" }, { t: 425, x: "Triangle.", a: "tr_01" },
            { t: 455, x: "Seated Meditation.", a: "sm_01" }, { t: 510, x: "Stillness is power.", a: "sm_03" }, { t: 545, x: "Supine Twist.", a: "su_01" },
            { t: 595, x: "Savasana.", a: "sa_01" }, { t: 620, x: "Rest completely.", a: "sa_02" }
        ];
        let GDS = GDS_B;
"""
# Replace const MAX_T = 640; through const GDS = ... ;
content = re.sub(r'const MAX_T = 640;.*?\];', const_def, content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
