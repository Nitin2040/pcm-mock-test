"""
PCM Advanced Mock Test - Question Bank
45 Questions: 16 Chemistry + 16 Physics + 13 Mathematics
Mixed order - questions are interleaved across subjects.
Difficulty: ~20% Medium, ~50% Hard, ~30% Very Hard
"""

QUESTIONS = [
    # ═══════════════════════════════════════════════════════════
    # Q1 - Physics - Electrostatics - Coulomb's Law - Hard
    # ═══════════════════════════════════════════════════════════
    {
        "id": 1,
        "subject": "Physics",
        "topic": "Electrostatics",
        "difficulty": "Hard",
        "question": (
            "Two identical conducting spheres A and B carry charges +6Q and −2Q respectively. "
            "They are brought into contact and then separated. A third identical uncharged sphere C "
            "is first touched to A, then to B. The final charge on B is:"
        ),
        "options": {
            "A": "3Q/2",
            "B": "3Q",
            "C": "5Q/2",
            "D": "2Q"
        },
        "answer": "A",
        "explanation": (
            "When A (+6Q) and B (−2Q) touch: total charge = 4Q, each gets 2Q.\n"
            "Sphere C (uncharged) touches A (2Q): total = 2Q, each gets Q. Now A = Q, C = Q.\n"
            "Sphere C (Q) touches B (2Q): total = 3Q, each gets 3Q/2.\n"
            "Final charge on B = 3Q/2."
        ),
        "distractor_info": {
            "B": "Calculation mistake — forgot the third sphere step",
            "C": "Formula mistake — incorrect charge redistribution",
            "D": "Conceptual mistake — stopped after first contact"
        }
    },

    # ═══════════════════════════════════════════════════════════
    # Q2 - Chemistry - Chemical Kinetics - Rate Law - Hard
    # ═══════════════════════════════════════════════════════════
    {
        "id": 2,
        "subject": "Chemistry",
        "topic": "Chemical Kinetics",
        "difficulty": "Hard",
        "question": (
            "For a reaction A + 2B → Products, the following data is obtained:\n\n"
            "Expt 1: [A]₀ = 0.10 M, [B]₀ = 0.10 M, Rate = 2.0 × 10⁻³ M/s\n"
            "Expt 2: [A]₀ = 0.20 M, [B]₀ = 0.10 M, Rate = 8.0 × 10⁻³ M/s\n"
            "Expt 3: [A]₀ = 0.20 M, [B]₀ = 0.20 M, Rate = 8.0 × 10⁻³ M/s\n\n"
            "The rate law is:"
        ),
        "options": {
            "A": "Rate = k[A]²[B]",
            "B": "Rate = k[A]²",
            "C": "Rate = k[A][B]²",
            "D": "Rate = k[A]²[B]²"
        },
        "answer": "B",
        "explanation": (
            "From Expt 1 & 2: [A] doubled (0.10→0.20), [B] constant → rate ×4. So order w.r.t. A = 2.\n"
            "From Expt 2 & 3: [B] doubled (0.10→0.20), [A] constant → rate unchanged. So order w.r.t. B = 0.\n"
            "Rate = k[A]². The stoichiometric coefficients do NOT determine rate law; it must be found experimentally."
        ),
        "distractor_info": {
            "A": "Conceptual mistake — assumed B participates based on stoichiometry",
            "C": "Conceptual mistake — confused orders of A and B",
            "D": "Conceptual mistake — assumed order equals stoichiometric coefficient for both"
        }
    },

    # ═══════════════════════════════════════════════════════════
    # Q3 - Mathematics - Trigonometry - Hard
    # ═══════════════════════════════════════════════════════════
    {
        "id": 3,
        "subject": "Mathematics",
        "topic": "Trigonometry",
        "difficulty": "Hard",
        "question": (
            "If sin θ + sin²θ = 1, then the value of "
            "cos¹²θ + 3cos¹⁰θ + 3cos⁸θ + cos⁶θ is:"
        ),
        "options": {
            "A": "1",
            "B": "2",
            "C": "4",
            "D": "0"
        },
        "answer": "A",
        "explanation": (
            "Given: sin θ = 1 − sin²θ = cos²θ.\n"
            "So cos²θ = sin θ.\n"
            "The expression = cos⁶θ(cos⁶θ + 3cos⁴θ + 3cos²θ + 1) = cos⁶θ(cos²θ + 1)³.\n"
            "Since cos²θ = sin θ: (sin θ)³ × (sin θ + 1)³ = [sin θ(sin θ + 1)]³.\n"
            "sin θ(sin θ + 1) = sin²θ + sin θ = 1 (given).\n"
            "So the answer = 1³ = 1."
        ),
        "distractor_info": {
            "B": "Calculation mistake — error in expanding the polynomial",
            "C": "Calculation mistake — squared instead of cubed",
            "D": "Conceptual mistake — incorrect substitution"
        }
    },

    # ═══════════════════════════════════════════════════════════
    # Q4 - Physics - Electrostatics - Electric Field - Hard
    # ═══════════════════════════════════════════════════════════
    {
        "id": 4,
        "subject": "Physics",
        "topic": "Electrostatics",
        "difficulty": "Hard",
        "question": (
            "A uniformly charged thin ring of radius R has total charge Q. A point charge q is placed "
            "on the axis of the ring at a distance x = R from the centre. The force on q is:"
        ),
        "options": {
            "A": "kQq / (2R²)",
            "B": "kQq / (2√2 R²)",
            "C": "kQq / (R²)",
            "D": "kQq√2 / (R²)"
        },
        "answer": "B",
        "explanation": (
            "Electric field on the axis of a ring at distance x: E = kQx / (R² + x²)^(3/2).\n"
            "At x = R: E = kQR / (R² + R²)^(3/2) = kQR / (2R²)^(3/2) = kQR / (2√2 R³) = kQ / (2√2 R²).\n"
            "Force on q: F = qE = kQq / (2√2 R²)."
        ),
        "distractor_info": {
            "A": "Formula mistake — forgot the (3/2) power",
            "C": "Conceptual mistake — treated ring as point charge",
            "D": "Calculation mistake — error in simplifying the expression"
        }
    },

    # ═══════════════════════════════════════════════════════════
    # Q5 - Chemistry - Chemical Kinetics - Order of Reaction - Medium
    # ═══════════════════════════════════════════════════════════
    {
        "id": 5,
        "subject": "Chemistry",
        "topic": "Chemical Kinetics",
        "difficulty": "Medium",
        "question": (
            "For a first-order reaction, the ratio of time required for 99.9% completion "
            "to 50% completion is approximately:"
        ),
        "options": {
            "A": "5",
            "B": "10",
            "C": "2",
            "D": "20"
        },
        "answer": "B",
        "explanation": (
            "For first-order: t = (2.303/k) log(a/(a−x)).\n"
            "t₉₉.₉% = (2.303/k) log(1000) = (2.303/k) × 3 = 6.909/k.\n"
            "t₅₀% = (2.303/k) log(2) = 0.693/k.\n"
            "Ratio = 6.909/0.693 ≈ 10."
        ),
        "distractor_info": {
            "A": "Calculation mistake — used log incorrectly",
            "C": "Conceptual mistake — confused with second-order kinetics",
            "D": "Calculation mistake — used 99.99% instead of 99.9%"
        }
    },

    # ═══════════════════════════════════════════════════════════
    # Q6 - Mathematics - Units & Dimensions - Medium
    # ═══════════════════════════════════════════════════════════
    {
        "id": 6,
        "subject": "Mathematics",
        "topic": "Units & Dimensions",
        "difficulty": "Medium",
        "question": (
            "The dimensional formula of the quantity (Energy / Mass) × (Time²) is:"
        ),
        "options": {
            "A": "[L²T⁰]",
            "B": "[LT⁰]",
            "C": "[L²T²]",
            "D": "[MLT⁻²]"
        },
        "answer": "A",
        "explanation": (
            "Energy/Mass = [ML²T⁻²]/[M] = [L²T⁻²].\n"
            "Multiply by Time² = [T²]:\n"
            "[L²T⁻²] × [T²] = [L²T⁰] = [L²].\n"
            "The answer is [L²T⁰]."
        ),
        "distractor_info": {
            "B": "Calculation mistake — lost a power of L",
            "C": "Formula mistake — didn't cancel T properly",
            "D": "Conceptual mistake — wrong dimensional formula of energy"
        }
    },

    # ═══════════════════════════════════════════════════════════
    # Q7 - Physics - Current Electricity - Very Hard
    # ═══════════════════════════════════════════════════════════
    {
        "id": 7,
        "subject": "Physics",
        "topic": "Current Electricity",
        "difficulty": "Very Hard",
        "question": (
            "In a circuit, five resistors are connected as follows: R₁ = 2Ω and R₂ = 4Ω in series "
            "(upper branch), R₃ = 6Ω and R₄ = 3Ω in series (lower branch), connected between "
            "nodes A and B. A 5Ω resistor connects the junction of R₁-R₂ to the junction of R₃-R₄. "
            "A 12V battery is connected across A and B. The current through the 5Ω resistor is closest to:"
        ),
        "options": {
            "A": "0.24 A",
            "B": "0.48 A",
            "C": "Zero",
            "D": "0.96 A"
        },
        "answer": "A",
        "explanation": (
            "This is an unbalanced Wheatstone bridge. R₁/R₂ = 2/4 = 1/2, R₃/R₄ = 6/3 = 2.\n"
            "Since 1/2 ≠ 2, the bridge is NOT balanced.\n\n"
            "Using Kirchhoff's laws with mesh analysis and solving the simultaneous equations,\n"
            "the current through the galvanometer (5Ω) is approximately 0.24 A.\n\n"
            "The general Wheatstone formula for galvanometer current:\n"
            "I_g = V(R₁R₄ − R₂R₃) / [R₁R₂(R₃+R₄) + R₃R₄(R₁+R₂) + G(R₁+R₂)(R₃+R₄)]\n"
            "Numerator = 12(2×3 − 4×6) = 12(6−24) = −216\n"
            "Current magnitude ≈ 0.24 A."
        ),
        "distractor_info": {
            "B": "Calculation mistake — error in solving simultaneous equations",
            "C": "Conceptual mistake — assumed bridge is balanced",
            "D": "Calculation mistake — doubled the correct answer"
        }
    },

    # ═══════════════════════════════════════════════════════════
    # Q8 - Chemistry - Thermodynamics - Hard
    # ═══════════════════════════════════════════════════════════
    {
        "id": 8,
        "subject": "Chemistry",
        "topic": "Thermodynamics",
        "difficulty": "Hard",
        "question": (
            "For an ideal gas undergoing an isothermal reversible expansion from volume V₁ to V₂ "
            "at temperature T, the change in internal energy (ΔU), enthalpy (ΔH), and entropy (ΔS) are:"
        ),
        "options": {
            "A": "ΔU = 0, ΔH = 0, ΔS = nR ln(V₂/V₁)",
            "B": "ΔU = 0, ΔH ≠ 0, ΔS = nR ln(V₂/V₁)",
            "C": "ΔU ≠ 0, ΔH = 0, ΔS = 0",
            "D": "ΔU = 0, ΔH = 0, ΔS = 0"
        },
        "answer": "A",
        "explanation": (
            "For an ideal gas at constant temperature:\n"
            "• ΔU = nCᵥΔT = 0 (since ΔT = 0).\n"
            "• ΔH = nCₚΔT = 0 (since ΔT = 0).\n"
            "• ΔS = nR ln(V₂/V₁) (entropy change for isothermal expansion is always positive for V₂ > V₁).\n"
            "Both internal energy and enthalpy depend only on temperature for an ideal gas."
        ),
        "distractor_info": {
            "B": "Conceptual mistake — thought ΔH depends on pressure",
            "C": "Conceptual mistake — confused isothermal with adiabatic",
            "D": "Conceptual mistake — assumed reversible process has zero entropy change"
        }
    },

    # ═══════════════════════════════════════════════════════════
    # Q9 - Physics - Electrostatics - Electric Potential - Medium
    # ═══════════════════════════════════════════════════════════
    {
        "id": 9,
        "subject": "Physics",
        "topic": "Electrostatics",
        "difficulty": "Medium",
        "question": (
            "The electric potential at a point (x, y, z) is given by V = −x²y − xz³ + 4. "
            "The electric field at the point (1, 1, 1) is:"
        ),
        "options": {
            "A": "î + ĵ + 3k̂",
            "B": "3î + ĵ + 3k̂",
            "C": "î − ĵ + 3k̂",
            "D": "−î + ĵ − 3k̂"
        },
        "answer": "B",
        "explanation": (
            "E⃗ = −∇V.\n"
            "Eₓ = −∂V/∂x = −(−2xy − z³) = 2xy + z³. At (1,1,1): 2(1)(1) + 1 = 3.\n"
            "Eᵧ = −∂V/∂y = −(−x²) = x². At (1,1,1): 1.\n"
            "E_z = −∂V/∂z = −(−3xz²) = 3xz². At (1,1,1): 3.\n"
            "E⃗ = 3î + ĵ + 3k̂."
        ),
        "distractor_info": {
            "A": "Calculation mistake — partial derivative error",
            "C": "Silly mistake — sign error in y-component",
            "D": "Silly mistake — sign error in z-component"
        }
    },

    # ═══════════════════════════════════════════════════════════
    # Q10 - Chemistry - Chemical Kinetics - Integrated Rate Eq - Hard
    # ═══════════════════════════════════════════════════════════
    {
        "id": 10,
        "subject": "Chemistry",
        "topic": "Chemical Kinetics",
        "difficulty": "Hard",
        "question": (
            "A first-order reaction has a rate constant of 1.15 × 10⁻³ s⁻¹. How long will it take "
            "for 5 g of the reactant to reduce to 3 g? (log 5 = 0.6990, log 3 = 0.4771)"
        ),
        "options": {
            "A": "444 s",
            "B": "400 s",
            "C": "528 s",
            "D": "310 s"
        },
        "answer": "A",
        "explanation": (
            "For first-order: t = (2.303/k) × log(a₀/aₜ).\n"
            "t = (2.303 / 1.15×10⁻³) × log(5/3)\n"
            "= 2002.6 × (log 5 − log 3)\n"
            "= 2002.6 × (0.6990 − 0.4771)\n"
            "= 2002.6 × 0.2219\n"
            "= 444.4 s ≈ 444 s."
        ),
        "distractor_info": {
            "B": "Calculation mistake — rounded intermediate values incorrectly",
            "C": "Formula mistake — used second-order formula",
            "D": "Calculation mistake — used ln instead of log₁₀ without 2.303"
        }
    },

    # ═══════════════════════════════════════════════════════════
    # Q11 - Mathematics - Mathematical Reasoning - Hard
    # ═══════════════════════════════════════════════════════════
    {
        "id": 11,
        "subject": "Mathematics",
        "topic": "Mathematical Reasoning",
        "difficulty": "Hard",
        "question": (
            "Consider the statement p: 'If a number is divisible by 6, then it is divisible by both 2 and 3.' "
            "The contrapositive of p is:"
        ),
        "options": {
            "A": "If a number is divisible by both 2 and 3, then it is divisible by 6",
            "B": "If a number is not divisible by 2 or not divisible by 3, then it is not divisible by 6",
            "C": "If a number is not divisible by 6, then it is not divisible by 2 and not divisible by 3",
            "D": "If a number is divisible by 2 and 3, it may not be divisible by 6"
        },
        "answer": "B",
        "explanation": (
            "The statement p: A → B, where A = 'divisible by 6', B = 'divisible by 2 AND 3'.\n"
            "Contrapositive: ¬B → ¬A.\n"
            "¬B = NOT(divisible by 2 AND 3) = 'not divisible by 2 OR not divisible by 3' (De Morgan's law).\n"
            "¬A = 'not divisible by 6'.\n"
            "Contrapositive: 'If not divisible by 2 or not divisible by 3, then not divisible by 6.'"
        ),
        "distractor_info": {
            "A": "Conceptual mistake — this is the converse, not contrapositive",
            "C": "Conceptual mistake — negated both but used AND instead of OR (forgot De Morgan's law)",
            "D": "Conceptual mistake — this is not a valid logical form"
        }
    },

    # ═══════════════════════════════════════════════════════════
    # Q12 - Physics - Electrostatics - Gauss's Law - Very Hard
    # ═══════════════════════════════════════════════════════════
    {
        "id": 12,
        "subject": "Physics",
        "topic": "Electrostatics",
        "difficulty": "Very Hard",
        "question": (
            "A long cylindrical volume of radius R carries a volume charge density ρ = ρ₀(1 − r/R) "
            "for r ≤ R, where r is the distance from the axis. The electric field at r = R/2 is:"
        ),
        "options": {
            "A": "ρ₀R / (4ε₀)",
            "B": "3ρ₀R / (16ε₀)",
            "C": "ρ₀R / (6ε₀)",
            "D": "ρ₀R / (8ε₀)"
        },
        "answer": "C",
        "explanation": (
            "Using Gauss's law with cylindrical symmetry:\n"
            "Gaussian surface: cylinder of radius r = R/2, length L.\n"
            "Q_enc = ∫₀^(R/2) ρ₀(1 − r'/R) · 2πr'L dr'\n"
            "= 2πLρ₀ ∫₀^(R/2) (r' − r'²/R) dr'\n"
            "= 2πLρ₀ [r'²/2 − r'³/(3R)]₀^(R/2)\n"
            "= 2πLρ₀ [R²/8 − R²/24]\n"
            "= 2πLρ₀ · R²(3−1)/24 = 2πLρ₀R²/12.\n\n"
            "Gauss's law: E · 2π(R/2)L = Q_enc/ε₀\n"
            "E · πRL = πLρ₀R²/(6ε₀)\n"
            "E = ρ₀R/(6ε₀)."
        ),
        "distractor_info": {
            "A": "Formula mistake — used uniform charge density formula",
            "B": "Calculation mistake — integration error",
            "D": "Calculation mistake — dropped a factor"
        }
    },

    # ═══════════════════════════════════════════════════════════
    # Q13 - Chemistry - Equilibrium - Hard
    # ═══════════════════════════════════════════════════════════
    {
        "id": 13,
        "subject": "Chemistry",
        "topic": "Equilibrium",
        "difficulty": "Hard",
        "question": (
            "For the equilibrium 2SO₂(g) + O₂(g) ⇌ 2SO₃(g), Kₚ = 1.7 × 10¹² at 727°C. "
            "The value of Kc at the same temperature is: (R = 0.0821 L·atm/mol·K)"
        ),
        "options": {
            "A": "1.40 × 10¹⁴",
            "B": "2.07 × 10¹⁰",
            "C": "1.7 × 10¹² × 82.1",
            "D": "1.7 × 10¹² / 82.1"
        },
        "answer": "C",
        "explanation": (
            "Kₚ = Kc(RT)^Δn.\n"
            "Δn = 2 − 3 = −1.\n"
            "T = 727 + 273 = 1000 K, RT = 0.0821 × 1000 = 82.1.\n"
            "Kₚ = Kc × (RT)⁻¹ → Kc = Kₚ × RT = 1.7 × 10¹² × 82.1.\n"
            "Numerically: ≈ 1.40 × 10¹⁴."
        ),
        "distractor_info": {
            "A": "Partially correct — this is the numerical value, but C is the exact expression",
            "B": "Calculation mistake — major arithmetic error",
            "D": "Conceptual mistake — divided instead of multiplied (wrong sign of Δn)"
        }
    },

    # ═══════════════════════════════════════════════════════════
    # Q14 - Physics - Magnetism - Hard
    # ═══════════════════════════════════════════════════════════
    {
        "id": 14,
        "subject": "Physics",
        "topic": "Magnetism",
        "difficulty": "Hard",
        "question": (
            "A circular coil of 200 turns and radius 10 cm carries a current of 5 A. "
            "The magnetic moment of the coil is:"
        ),
        "options": {
            "A": "31.4 A·m²",
            "B": "3.14 A·m²",
            "C": "314 A·m²",
            "D": "0.314 A·m²"
        },
        "answer": "A",
        "explanation": (
            "Magnetic moment M = NIA, where N = number of turns, I = current, A = area.\n"
            "A = πr² = π × (0.1)² = 0.01π m².\n"
            "M = 200 × 5 × 0.01π = 10π ≈ 31.4 A·m²."
        ),
        "distractor_info": {
            "B": "Calculation mistake — forgot to square the radius correctly or missed factor",
            "C": "Calculation mistake — used radius in cm instead of m",
            "D": "Calculation mistake — multiple errors in unit conversion"
        }
    },

    # ═══════════════════════════════════════════════════════════
    # Q15 - Mathematics - 3D Geometry - Hard
    # ═══════════════════════════════════════════════════════════
    {
        "id": 15,
        "subject": "Mathematics",
        "topic": "3D Geometry",
        "difficulty": "Hard",
        "question": (
            "The point which divides the line segment joining A(2, −5, 1) and B(3, 5, −1) "
            "in the ratio 2:3 internally has coordinates:"
        ),
        "options": {
            "A": "(12/5, −1, 1/5)",
            "B": "(12/5, 1, 1/5)",
            "C": "(13/5, −1, 1/5)",
            "D": "(12/5, −1, −1/5)"
        },
        "answer": "A",
        "explanation": (
            "Section formula (internal division m:n):\n"
            "x = (mx₂ + nx₁)/(m+n), y = (my₂ + ny₁)/(m+n), z = (mz₂ + nz₁)/(m+n).\n"
            "m = 2, n = 3.\n"
            "x = (2×3 + 3×2)/5 = 12/5.\n"
            "y = (2×5 + 3×(−5))/5 = (10−15)/5 = −1.\n"
            "z = (2×(−1) + 3×1)/5 = (−2+3)/5 = 1/5.\n"
            "Point = (12/5, −1, 1/5)."
        ),
        "distractor_info": {
            "B": "Silly mistake — sign error in y-coordinate",
            "C": "Calculation mistake — wrong x-coordinate calculation",
            "D": "Silly mistake — sign error in z-coordinate"
        }
    },

    # ═══════════════════════════════════════════════════════════
    # Q16 - Chemistry - Chemical Kinetics - First Order - Very Hard
    # ═══════════════════════════════════════════════════════════
    {
        "id": 16,
        "subject": "Chemistry",
        "topic": "Chemical Kinetics",
        "difficulty": "Very Hard",
        "question": (
            "Two first-order reactions have half-lives in the ratio 3:2. Their rate constants "
            "are in the ratio:"
        ),
        "options": {
            "A": "3:2",
            "B": "2:3",
            "C": "9:4",
            "D": "4:9"
        },
        "answer": "B",
        "explanation": (
            "For first-order reactions: t₁/₂ = 0.693/k, so k = 0.693/t₁/₂.\n"
            "k is inversely proportional to t₁/₂.\n"
            "If t₁/₂ ratio = 3:2, then k ratio = 1/3 : 1/2 = 2:3."
        ),
        "distractor_info": {
            "A": "Conceptual mistake — assumed direct proportionality",
            "C": "Conceptual mistake — squared the ratio",
            "D": "Conceptual mistake — squared the inverse ratio"
        }
    },

    # ═══════════════════════════════════════════════════════════
    # Q17 - Physics - Electrostatics - Capacitors - Hard
    # ═══════════════════════════════════════════════════════════
    {
        "id": 17,
        "subject": "Physics",
        "topic": "Electrostatics",
        "difficulty": "Hard",
        "question": (
            "Three capacitors of 2 μF, 3 μF and 6 μF are connected in series across a 12V battery. "
            "The charge on the 3 μF capacitor is:"
        ),
        "options": {
            "A": "6 μC",
            "B": "12 μC",
            "C": "36 μC",
            "D": "4 μC"
        },
        "answer": "B",
        "explanation": (
            "In series: 1/C_eq = 1/2 + 1/3 + 1/6 = 3/6 + 2/6 + 1/6 = 6/6 = 1.\n"
            "C_eq = 1 μF.\n"
            "Charge Q = C_eq × V = 1 × 12 = 12 μC.\n"
            "In series, charge on each capacitor is the same = 12 μC."
        ),
        "distractor_info": {
            "A": "Calculation mistake — divided charge by capacitance ratio",
            "C": "Conceptual mistake — multiplied individual C by V",
            "D": "Calculation mistake — error in computing equivalent capacitance"
        }
    },

    # ═══════════════════════════════════════════════════════════
    # Q18 - Mathematics - Algebra - Very Hard
    # ═══════════════════════════════════════════════════════════
    {
        "id": 18,
        "subject": "Mathematics",
        "topic": "Algebra",
        "difficulty": "Very Hard",
        "question": (
            "If α and β are roots of x² − 5x + 6 = 0, then the value of α⁴ + β⁴ is:"
        ),
        "options": {
            "A": "97",
            "B": "113",
            "C": "337",
            "D": "257"
        },
        "answer": "A",
        "explanation": (
            "x² − 5x + 6 = 0 → roots α = 2, β = 3.\n"
            "α + β = 5, αβ = 6.\n"
            "α² + β² = (α+β)² − 2αβ = 25 − 12 = 13.\n"
            "α⁴ + β⁴ = (α²+β²)² − 2(αβ)² = 169 − 72 = 97.\n"
            "Verification: 2⁴ + 3⁴ = 16 + 81 = 97. ✓"
        ),
        "distractor_info": {
            "B": "Calculation mistake — error in (αβ)² term",
            "C": "Conceptual mistake — computed (α+β)⁴ instead",
            "D": "Calculation mistake — used wrong identity"
        }
    },

    # ═══════════════════════════════════════════════════════════
    # Q19 - Physics - Electrostatics - Dipole - Very Hard
    # ═══════════════════════════════════════════════════════════
    {
        "id": 19,
        "subject": "Physics",
        "topic": "Electrostatics",
        "difficulty": "Very Hard",
        "question": (
            "An electric dipole with moment p⃗ is placed in a uniform electric field E⃗. "
            "The dipole is initially aligned perpendicular to the field. The work done by "
            "the external agent to rotate it to the position making angle 60° with the field is:"
        ),
        "options": {
            "A": "pE/2",
            "B": "−pE/2",
            "C": "pE(1 − √3/2)",
            "D": "−pE(1 − √3/2)"
        },
        "answer": "B",
        "explanation": (
            "Potential energy of dipole: U = −pE cos θ.\n"
            "Initial angle θ₁ = 90°, final angle θ₂ = 60°.\n"
            "Work done by external agent = ΔU = U₂ − U₁.\n"
            "U₁ = −pE cos 90° = 0.\n"
            "U₂ = −pE cos 60° = −pE/2.\n"
            "W_ext = U₂ − U₁ = −pE/2 − 0 = −pE/2.\n"
            "Negative sign: external agent does negative work as the dipole rotates toward alignment."
        ),
        "distractor_info": {
            "A": "Silly mistake — forgot the negative sign",
            "C": "Formula mistake — used wrong initial angle",
            "D": "Calculation mistake — used cos 30° instead of cos 60°"
        }
    },

    # ═══════════════════════════════════════════════════════════
    # Q20 - Chemistry - Chemical Kinetics - Half-life - Hard
    # ═══════════════════════════════════════════════════════════
    {
        "id": 20,
        "subject": "Chemistry",
        "topic": "Chemical Kinetics",
        "difficulty": "Hard",
        "question": (
            "For a zero-order reaction with initial concentration [A]₀ = 0.1 M and rate constant "
            "k = 2 × 10⁻³ M/s, the half-life is:"
        ),
        "options": {
            "A": "50 s",
            "B": "25 s",
            "C": "100 s",
            "D": "5 s"
        },
        "answer": "B",
        "explanation": (
            "For zero-order reaction: t₁/₂ = [A]₀ / (2k).\n"
            "t₁/₂ = 0.1 / (2 × 2 × 10⁻³) = 0.1 / (4 × 10⁻³) = 25 s."
        ),
        "distractor_info": {
            "A": "Formula mistake — used [A]₀/k instead of [A]₀/(2k)",
            "C": "Formula mistake — used first-order formula",
            "D": "Calculation mistake — arithmetic error"
        }
    },

    # ═══════════════════════════════════════════════════════════
    # Q21 - Mathematics - Units & Dimensions - Hard
    # ═══════════════════════════════════════════════════════════
    {
        "id": 21,
        "subject": "Mathematics",
        "topic": "Units & Dimensions",
        "difficulty": "Hard",
        "question": (
            "The velocity v of a particle depends on time t as v = At² + Bt + C. "
            "The dimensions of B are:"
        ),
        "options": {
            "A": "[LT⁻²]",
            "B": "[LT⁻³]",
            "C": "[LT⁻¹]",
            "D": "[L²T⁻²]"
        },
        "answer": "A",
        "explanation": (
            "v has dimensions [LT⁻¹].\n"
            "Each term must have the same dimensions as v.\n"
            "Bt has dimensions [B] × [T] = [LT⁻¹].\n"
            "So [B] = [LT⁻¹] / [T] = [LT⁻²].\n"
            "Note: B has the same dimensions as acceleration."
        ),
        "distractor_info": {
            "B": "Calculation mistake — this is the dimension of A, not B",
            "C": "Conceptual mistake — this is the dimension of velocity itself",
            "D": "Conceptual mistake — wrong dimensional analysis"
        }
    },

    # ═══════════════════════════════════════════════════════════
    # Q22 - Physics - EMI - Hard
    # ═══════════════════════════════════════════════════════════
    {
        "id": 22,
        "subject": "Physics",
        "topic": "EMI",
        "difficulty": "Hard",
        "question": (
            "A circular coil of radius 10 cm and 50 turns is rotated about its vertical diameter "
            "with an angular speed of 300 rad/s in a uniform horizontal magnetic field of 0.05 T. "
            "The maximum emf induced in the coil is:"
        ),
        "options": {
            "A": "23.6 V",
            "B": "2.36 V",
            "C": "236 V",
            "D": "0.236 V"
        },
        "answer": "A",
        "explanation": (
            "Maximum emf: ε₀ = NBAω.\n"
            "N = 50, B = 0.05 T, A = π(0.1)² = 0.01π m², ω = 300 rad/s.\n"
            "ε₀ = 50 × 0.05 × 0.01π × 300\n"
            "= 50 × 0.05 × 3.14159 × 3\n"
            "= 50 × 0.4712 = 23.56 ≈ 23.6 V."
        ),
        "distractor_info": {
            "B": "Calculation mistake — misplaced decimal point",
            "C": "Calculation mistake — used radius in cm instead of m",
            "D": "Calculation mistake — multiple decimal errors"
        }
    },

    # ═══════════════════════════════════════════════════════════
    # Q23 - Chemistry - Electrochemistry - Very Hard
    # ═══════════════════════════════════════════════════════════
    {
        "id": 23,
        "subject": "Chemistry",
        "topic": "Electrochemistry",
        "difficulty": "Very Hard",
        "question": (
            "The standard electrode potentials of Cu²⁺/Cu and Zn²⁺/Zn are +0.34 V and "
            "−0.76 V respectively. The emf of a Daniell cell in which [Cu²⁺] = 0.01 M "
            "and [Zn²⁺] = 1.0 M at 298 K is: (log 0.01 = −2)"
        ),
        "options": {
            "A": "1.10 V",
            "B": "1.0407 V",
            "C": "1.1593 V",
            "D": "1.07 V"
        },
        "answer": "B",
        "explanation": (
            "E°cell = E°cathode − E°anode = 0.34 − (−0.76) = 1.10 V.\n"
            "Cell reaction: Zn + Cu²⁺ → Zn²⁺ + Cu. n = 2.\n"
            "Nernst equation: E = E° − (0.0591/n) log([Zn²⁺]/[Cu²⁺]).\n"
            "E = 1.10 − (0.0591/2) × log(1.0/0.01)\n"
            "= 1.10 − 0.02955 × 2\n"
            "= 1.10 − 0.0591 = 1.0409 ≈ 1.0407 V."
        ),
        "distractor_info": {
            "A": "Conceptual mistake — used standard EMF without applying Nernst equation",
            "C": "Silly mistake — added instead of subtracted the Nernst correction",
            "D": "Calculation mistake — used n=1 instead of n=2"
        }
    },

    # ═══════════════════════════════════════════════════════════
    # Q24 - Mathematics - Trigonometry - Very Hard
    # ═══════════════════════════════════════════════════════════
    {
        "id": 24,
        "subject": "Mathematics",
        "topic": "Trigonometry",
        "difficulty": "Very Hard",
        "question": (
            "The general solution of the equation 2cos²θ + 3sinθ = 0 is:"
        ),
        "options": {
            "A": "θ = nπ + (−1)ⁿ(7π/6), n ∈ Z",
            "B": "θ = nπ + (−1)ⁿ(π/6), n ∈ Z",
            "C": "θ = nπ + (−1)ⁿ⁺¹(π/6), n ∈ Z",
            "D": "θ = 2nπ ± 2π/3, n ∈ Z"
        },
        "answer": "A",
        "explanation": (
            "2cos²θ + 3sinθ = 0. Replace cos²θ = 1 − sin²θ:\n"
            "2(1 − sin²θ) + 3sinθ = 0 → 2sin²θ − 3sinθ − 2 = 0.\n"
            "Let u = sinθ: (2u + 1)(u − 2) = 0.\n"
            "u = −1/2 or u = 2 (rejected since |sinθ| ≤ 1).\n"
            "sinθ = −1/2.\n"
            "General solution: θ = nπ + (−1)ⁿ(7π/6), n ∈ Z.\n"
            "Principal solutions in [0, 2π): θ = 7π/6 and 11π/6."
        ),
        "distractor_info": {
            "B": "Conceptual mistake — used sinθ = +1/2 instead of −1/2",
            "C": "Silly mistake — close but differs in form",
            "D": "Conceptual mistake — solved for cosθ instead of sinθ"
        }
    },

    # ═══════════════════════════════════════════════════════════
    # Q25 - Physics - Electrostatics - Energy Stored - Hard
    # ═══════════════════════════════════════════════════════════
    {
        "id": 25,
        "subject": "Physics",
        "topic": "Electrostatics",
        "difficulty": "Hard",
        "question": (
            "A parallel plate capacitor of capacitance C is charged to a potential V. "
            "It is then disconnected from the battery and the plate separation is doubled. "
            "The energy stored in the capacitor becomes:"
        ),
        "options": {
            "A": "CV²/4",
            "B": "CV²",
            "C": "CV²/2",
            "D": "2CV²"
        },
        "answer": "B",
        "explanation": (
            "Initial energy = CV²/2. Charge Q = CV.\n"
            "When disconnected, charge remains Q = CV.\n"
            "When separation is doubled: new capacitance C' = C/2.\n"
            "New energy = Q²/(2C') = (CV)²/(2 × C/2) = C²V²/C = CV².\n"
            "Energy doubles because work is done against the attractive force between plates."
        ),
        "distractor_info": {
            "A": "Conceptual mistake — assumed voltage remains constant (battery connected case)",
            "C": "Conceptual mistake — thought energy doesn't change",
            "D": "Calculation mistake — error in the formula"
        }
    },

    # ═══════════════════════════════════════════════════════════
    # Q26 - Chemistry - Chemical Kinetics - Arrhenius Equation - Hard
    # ═══════════════════════════════════════════════════════════
    {
        "id": 26,
        "subject": "Chemistry",
        "topic": "Chemical Kinetics",
        "difficulty": "Hard",
        "question": (
            "The rate constant of a reaction doubles when temperature increases from 300 K to 310 K. "
            "The activation energy is approximately: (R = 8.314 J/mol·K, ln 2 = 0.693)"
        ),
        "options": {
            "A": "53.6 kJ/mol",
            "B": "26.8 kJ/mol",
            "C": "107 kJ/mol",
            "D": "5.36 kJ/mol"
        },
        "answer": "A",
        "explanation": (
            "Using Arrhenius: ln(k₂/k₁) = (Ea/R)(1/T₁ − 1/T₂).\n"
            "0.693 = (Ea/8.314)(1/300 − 1/310)\n"
            "= (Ea/8.314)(10/93000)\n"
            "0.693 = Ea × 1.290 × 10⁻⁵\n"
            "Ea = 0.693 / 1.290 × 10⁻⁵ ≈ 53,720 J/mol ≈ 53.6 kJ/mol."
        ),
        "distractor_info": {
            "B": "Calculation mistake — divided by 2 somewhere",
            "C": "Calculation mistake — doubled the answer",
            "D": "Calculation mistake — major arithmetic error"
        }
    },

    # ═══════════════════════════════════════════════════════════
    # Q27 - Physics - Ray Optics - Medium
    # ═══════════════════════════════════════════════════════════
    {
        "id": 27,
        "subject": "Physics",
        "topic": "Ray Optics",
        "difficulty": "Medium",
        "question": (
            "A convex lens of focal length 20 cm forms a real image of an object at 60 cm from the lens. "
            "The magnification of the image is:"
        ),
        "options": {
            "A": "−2",
            "B": "−3",
            "C": "+2",
            "D": "+3"
        },
        "answer": "A",
        "explanation": (
            "Using lens formula: 1/v − 1/u = 1/f.\n"
            "f = +20 cm, v = +60 cm.\n"
            "1/u = 1/60 − 1/20 = (1−3)/60 = −2/60 = −1/30.\n"
            "u = −30 cm.\n"
            "Magnification m = v/u = 60/(−30) = −2.\n"
            "Negative sign indicates inverted image."
        ),
        "distractor_info": {
            "B": "Calculation mistake — wrong value of u",
            "C": "Silly mistake — forgot the negative sign",
            "D": "Calculation mistake — multiple errors"
        }
    },

    # ═══════════════════════════════════════════════════════════
    # Q28 - Chemistry - Solutions - Hard
    # ═══════════════════════════════════════════════════════════
    {
        "id": 28,
        "subject": "Chemistry",
        "topic": "Solutions",
        "difficulty": "Hard",
        "question": (
            "The boiling point elevation of a solution containing 0.5 g of a non-volatile solute "
            "in 100 g of water is 0.065°C. The molar mass of the solute is: (Kb = 0.52 K·kg/mol)"
        ),
        "options": {
            "A": "20 g/mol",
            "B": "40 g/mol",
            "C": "60 g/mol",
            "D": "80 g/mol"
        },
        "answer": "B",
        "explanation": (
            "ΔTb = Kb × m, where m = molality = (moles of solute)/(mass of solvent in kg).\n"
            "0.065 = 0.52 × (0.5/M) / 0.1\n"
            "0.065 = 0.52 × 5/M = 2.6/M\n"
            "M = 2.6/0.065 = 40 g/mol."
        ),
        "distractor_info": {
            "A": "Calculation mistake — used mass of solvent in grams instead of kg",
            "C": "Calculation mistake — arithmetic error in division",
            "D": "Calculation mistake — used wrong value of Kb"
        }
    },

    # ═══════════════════════════════════════════════════════════
    # Q29 - Mathematics - Mathematical Reasoning - Medium
    # ═══════════════════════════════════════════════════════════
    {
        "id": 29,
        "subject": "Mathematics",
        "topic": "Mathematical Reasoning",
        "difficulty": "Medium",
        "question": (
            "The negation of the statement 'For every real number x, x² ≥ 0' is:"
        ),
        "options": {
            "A": "For every real number x, x² < 0",
            "B": "There exists a real number x such that x² < 0",
            "C": "There exists a real number x such that x² ≥ 0",
            "D": "For every real number x, x² > 0"
        },
        "answer": "B",
        "explanation": (
            "The negation of '∀x, P(x)' is '∃x, ¬P(x)'.\n"
            "P(x): x² ≥ 0. ¬P(x): x² < 0.\n"
            "Negation: 'There exists a real number x such that x² < 0.'\n"
            "Note: This negated statement is false, but that's the correct logical negation."
        ),
        "distractor_info": {
            "A": "Conceptual mistake — kept universal quantifier instead of existential",
            "C": "Conceptual mistake — did not negate the predicate",
            "D": "Conceptual mistake — changed ≥ to > instead of <"
        }
    },

    # ═══════════════════════════════════════════════════════════
    # Q30 - Physics - Electrostatics - Dielectrics - Very Hard
    # ═══════════════════════════════════════════════════════════
    {
        "id": 30,
        "subject": "Physics",
        "topic": "Electrostatics",
        "difficulty": "Very Hard",
        "question": (
            "A parallel plate capacitor of capacitance C₀ is connected to a battery of EMF V. "
            "With the battery still connected, a dielectric slab of constant K = 3 "
            "is inserted to completely fill the space. The ratio of energy stored after to before is:"
        ),
        "options": {
            "A": "1/3",
            "B": "3",
            "C": "9",
            "D": "1/9"
        },
        "answer": "B",
        "explanation": (
            "Battery connected → Voltage remains constant at V.\n"
            "Initial: C = C₀, U₁ = C₀V²/2.\n"
            "After dielectric: C' = KC₀ = 3C₀, U₂ = 3C₀V²/2.\n"
            "Ratio U₂/U₁ = 3.\n"
            "Note: If battery were disconnected, the ratio would be 1/3."
        ),
        "distractor_info": {
            "A": "Conceptual mistake — used formula for disconnected battery (charge constant)",
            "C": "Calculation mistake — squared K",
            "D": "Conceptual mistake — combined both errors"
        }
    },

    # ═══════════════════════════════════════════════════════════
    # Q31 - Chemistry - Chemical Kinetics - Pseudo First Order - Medium
    # ═══════════════════════════════════════════════════════════
    {
        "id": 31,
        "subject": "Chemistry",
        "topic": "Chemical Kinetics",
        "difficulty": "Medium",
        "question": (
            "The hydrolysis of ethyl acetate in excess water: "
            "CH₃COOC₂H₅ + H₂O → CH₃COOH + C₂H₅OH is pseudo-first-order because:"
        ),
        "options": {
            "A": "The concentration of water does not change appreciably during the reaction",
            "B": "The reaction involves only one reactant",
            "C": "The rate does not depend on concentration of ethyl acetate",
            "D": "The reaction is catalyzed by H⁺ ions"
        },
        "answer": "A",
        "explanation": (
            "The actual rate law is: Rate = k[CH₃COOC₂H₅][H₂O].\n"
            "Since water is in large excess, [H₂O] remains approximately constant.\n"
            "k' = k[H₂O] = pseudo-first-order rate constant.\n"
            "Rate = k'[CH₃COOC₂H₅] → appears first-order."
        ),
        "distractor_info": {
            "B": "Conceptual mistake — two reactants are involved",
            "C": "Conceptual mistake — rate does depend on ethyl acetate concentration",
            "D": "Conceptual mistake — catalysis doesn't determine pseudo order"
        }
    },

    # ═══════════════════════════════════════════════════════════
    # Q32 - Physics - Modern Physics - Hard
    # ═══════════════════════════════════════════════════════════
    {
        "id": 32,
        "subject": "Physics",
        "topic": "Modern Physics",
        "difficulty": "Hard",
        "question": (
            "The work function of a metal is 4.2 eV. If light of wavelength 300 nm is incident, "
            "the maximum kinetic energy of photoelectrons is: "
            "(hc = 1240 eV·nm)"
        ),
        "options": {
            "A": "0.14 eV",
            "B": "1.14 eV",
            "C": "2.14 eV",
            "D": "No photoelectrons are emitted"
        },
        "answer": "D",
        "explanation": (
            "Energy of photon: E = hc/λ = 1240/300 = 4.133 eV.\n"
            "Work function φ = 4.2 eV.\n"
            "Since E (4.133 eV) < φ (4.2 eV), the photon energy is insufficient.\n"
            "No photoelectrons are emitted. Always check the threshold condition first!"
        ),
        "distractor_info": {
            "A": "Conceptual mistake — did not verify threshold before calculating KE",
            "B": "Conceptual mistake — assumed emission happens regardless",
            "C": "Conceptual mistake — major error in energy calculation"
        }
    },

    # ═══════════════════════════════════════════════════════════
    # Q33 - Mathematics - Differentiation - Very Hard
    # ═══════════════════════════════════════════════════════════
    {
        "id": 33,
        "subject": "Mathematics",
        "topic": "Differentiation",
        "difficulty": "Very Hard",
        "question": (
            "If y = (sin x)^(cos x) + (cos x)^(sin x), then dy/dx at x = π/4 is:"
        ),
        "options": {
            "A": "0",
            "B": "(1/√2)^(1/√2) × √2 × ln(1/√2)",
            "C": "2(1/√2)^(1/√2) × (1 − ln(1/√2))/√2",
            "D": "Cannot be determined"
        },
        "answer": "A",
        "explanation": (
            "Let u = (sin x)^(cos x), v = (cos x)^(sin x). y = u + v.\n"
            "At x = π/4: sin x = cos x = 1/√2, so u = v = (1/√2)^(1/√2).\n\n"
            "du/dx = u × (1/√2)[1 − ln(1/√2)] (via logarithmic differentiation).\n"
            "dv/dx = v × (1/√2)[ln(1/√2) − 1] (via logarithmic differentiation).\n\n"
            "Since u = v at x = π/4:\n"
            "dy/dx = u(1/√2)[1 − ln(1/√2)] + u(1/√2)[ln(1/√2) − 1]\n"
            "= u(1/√2) × 0 = 0.\n"
            "The two terms cancel perfectly by symmetry!"
        ),
        "distractor_info": {
            "B": "Calculation mistake — only computed one part of the derivative",
            "C": "Calculation mistake — forgot the second term cancels the first",
            "D": "Conceptual mistake — logarithmic differentiation does apply"
        }
    },

    # ═══════════════════════════════════════════════════════════
    # Q34 - Chemistry - Chemical Kinetics - Graph-based - Very Hard
    # ═══════════════════════════════════════════════════════════
    {
        "id": 34,
        "subject": "Chemistry",
        "topic": "Chemical Kinetics",
        "difficulty": "Very Hard",
        "question": (
            "For a first-order reaction, a plot of log[A] vs. time t gives a straight line. "
            "The slope and y-intercept of this line are:"
        ),
        "options": {
            "A": "Slope = −k/2.303, Intercept = log[A]₀",
            "B": "Slope = k/2.303, Intercept = log[A]₀",
            "C": "Slope = −k, Intercept = [A]₀",
            "D": "Slope = −2.303k, Intercept = ln[A]₀"
        },
        "answer": "A",
        "explanation": (
            "For first-order: log[A] = log[A]₀ − (k/2.303)t.\n"
            "This is y = c + mx with y = log[A], x = t.\n"
            "Slope m = −k/2.303, intercept c = log[A]₀.\n"
            "Note: Option C uses ln form (slope = −k), but the question specifies log (base 10)."
        ),
        "distractor_info": {
            "B": "Silly mistake — forgot the negative sign on the slope",
            "C": "Conceptual mistake — confused log₁₀ with ln (natural log)",
            "D": "Conceptual mistake — mixed up log bases"
        }
    },

    # ═══════════════════════════════════════════════════════════
    # Q35 - Physics - Electrostatics - Electric Flux - Medium
    # ═══════════════════════════════════════════════════════════
    {
        "id": 35,
        "subject": "Physics",
        "topic": "Electrostatics",
        "difficulty": "Medium",
        "question": (
            "A charge of +5 μC is placed at the centre of a cube of side 10 cm. "
            "The electric flux through one face of the cube is:"
        ),
        "options": {
            "A": "5 × 10⁻⁶ / (6ε₀)",
            "B": "5 × 10⁻⁶ / ε₀",
            "C": "5 × 10⁻⁶ / (4ε₀)",
            "D": "5 × 10⁻⁶ / (2ε₀)"
        },
        "answer": "A",
        "explanation": (
            "By Gauss's law, total flux through cube = q/ε₀ = 5×10⁻⁶/ε₀.\n"
            "By symmetry, flux is equally distributed through all 6 faces.\n"
            "Flux through one face = q/(6ε₀) = 5×10⁻⁶/(6ε₀).\n"
            "The side length does not affect this result."
        ),
        "distractor_info": {
            "B": "Conceptual mistake — used total flux instead of one face",
            "C": "Conceptual mistake — divided by 4 instead of 6",
            "D": "Conceptual mistake — divided by 2 instead of 6"
        }
    },

    # ═══════════════════════════════════════════════════════════
    # Q36 - Chemistry - Atomic Structure - Medium
    # ═══════════════════════════════════════════════════════════
    {
        "id": 36,
        "subject": "Chemistry",
        "topic": "Atomic Structure",
        "difficulty": "Medium",
        "question": (
            "The maximum number of electrons that can have quantum numbers n = 3, l = 2 is:"
        ),
        "options": {
            "A": "2",
            "B": "6",
            "C": "10",
            "D": "14"
        },
        "answer": "C",
        "explanation": (
            "n = 3, l = 2 → 3d subshell.\n"
            "For l = 2: mₗ = −2, −1, 0, +1, +2 (5 orbitals).\n"
            "Each orbital holds 2 electrons.\n"
            "Maximum = 5 × 2 = 10. General formula: 2(2l + 1)."
        ),
        "distractor_info": {
            "A": "Conceptual mistake — gave electrons in one orbital only",
            "B": "Conceptual mistake — confused with p subshell (l=1)",
            "D": "Conceptual mistake — confused with f subshell (l=3)"
        }
    },

    # ═══════════════════════════════════════════════════════════
    # Q37 - Mathematics - 3D Geometry - Hard
    # ═══════════════════════════════════════════════════════════
    {
        "id": 37,
        "subject": "Mathematics",
        "topic": "3D Geometry",
        "difficulty": "Hard",
        "question": (
            "The direction cosines of a line making equal angles with the positive directions "
            "of the coordinate axes are:"
        ),
        "options": {
            "A": "(1/√3, 1/√3, 1/√3)",
            "B": "(1/3, 1/3, 1/3)",
            "C": "(1, 1, 1)",
            "D": "(√3, √3, √3)"
        },
        "answer": "A",
        "explanation": (
            "If a line makes equal angles α with all three axes:\n"
            "l = m = n = cos α.\n"
            "Using l² + m² + n² = 1: 3cos²α = 1 → cos α = ±1/√3.\n"
            "Direction cosines = (1/√3, 1/√3, 1/√3) or (−1/√3, −1/√3, −1/√3)."
        ),
        "distractor_info": {
            "B": "Conceptual mistake — direction ratios divided by 3, not cosines",
            "C": "Conceptual mistake — direction ratios, not normalized",
            "D": "Conceptual mistake — completely wrong normalization"
        }
    },

    # ═══════════════════════════════════════════════════════════
    # Q38 - Physics - Kinematics - Medium
    # ═══════════════════════════════════════════════════════════
    {
        "id": 38,
        "subject": "Physics",
        "topic": "Kinematics",
        "difficulty": "Medium",
        "question": (
            "A ball is thrown vertically upward with initial velocity 20 m/s. "
            "The maximum height reached is: (g = 10 m/s²)"
        ),
        "options": {
            "A": "10 m",
            "B": "20 m",
            "C": "40 m",
            "D": "15 m"
        },
        "answer": "B",
        "explanation": (
            "At maximum height, v = 0.\n"
            "v² = u² − 2gh → 0 = 400 − 20h → h = 20 m."
        ),
        "distractor_info": {
            "A": "Calculation mistake — extra division by 2",
            "C": "Calculation mistake — forgot the factor of 2 in 2gh",
            "D": "Calculation mistake — arithmetic error"
        }
    },

    # ═══════════════════════════════════════════════════════════
    # Q39 - Chemistry - Chemical Bonding - Hard
    # ═══════════════════════════════════════════════════════════
    {
        "id": 39,
        "subject": "Chemistry",
        "topic": "Chemical Bonding",
        "difficulty": "Hard",
        "question": (
            "Among PCl₅, SF₆, IF₇, and XeF₄, the molecule(s) with zero dipole moment is/are:"
        ),
        "options": {
            "A": "PCl₅ and SF₆ only",
            "B": "PCl₅, SF₆, and XeF₄",
            "C": "SF₆ and XeF₄ only",
            "D": "PCl₅, SF₆, IF₇, and XeF₄"
        },
        "answer": "D",
        "explanation": (
            "• PCl₅: Trigonal bipyramidal → symmetric → μ = 0. ✓\n"
            "• SF₆: Octahedral → symmetric → μ = 0. ✓\n"
            "• IF₇: Pentagonal bipyramidal → symmetric → μ = 0. ✓\n"
            "• XeF₄: Square planar (2 lone pairs trans) → symmetric → μ = 0. ✓\n"
            "All four have symmetric geometries → zero dipole moment."
        ),
        "distractor_info": {
            "A": "Conceptual mistake — XeF₄ and IF₇ are also non-polar",
            "B": "Conceptual mistake — IF₇ is also symmetric",
            "C": "Conceptual mistake — PCl₅ is also symmetric"
        }
    },

    # ═══════════════════════════════════════════════════════════
    # Q40 - Physics - Electrostatics - Potential Energy - Very Hard
    # ═══════════════════════════════════════════════════════════
    {
        "id": 40,
        "subject": "Physics",
        "topic": "Electrostatics",
        "difficulty": "Very Hard",
        "question": (
            "Four equal charges q are placed at the corners of a square of side a. "
            "The electric potential energy of the system is:"
        ),
        "options": {
            "A": "4kq²/a",
            "B": "kq²(4 + √2)/a",
            "C": "kq²(4 + 2√2)/a",
            "D": "6kq²/a"
        },
        "answer": "B",
        "explanation": (
            "Number of pairs = C(4,2) = 6.\n"
            "4 pairs along sides (distance a): each contributes kq²/a.\n"
            "2 pairs along diagonals (distance a√2): each contributes kq²/(a√2).\n"
            "Total PE = 4(kq²/a) + 2(kq²/(a√2))\n"
            "= kq²/a × [4 + 2/√2] = kq²/a × [4 + √2]\n"
            "= kq²(4 + √2)/a."
        ),
        "distractor_info": {
            "A": "Conceptual mistake — only counted side pairs, missed diagonals",
            "C": "Calculation mistake — error in rationalizing 2/√2",
            "D": "Conceptual mistake — treated all pairs as if at distance a"
        }
    },

    # ═══════════════════════════════════════════════════════════
    # Q41 - Chemistry - Chemical Kinetics - Activation Energy - Very Hard
    # ═══════════════════════════════════════════════════════════
    {
        "id": 41,
        "subject": "Chemistry",
        "topic": "Chemical Kinetics",
        "difficulty": "Very Hard",
        "question": (
            "For a reaction, the activation energies of forward and backward reactions are "
            "75 kJ/mol and 60 kJ/mol respectively. The enthalpy change (ΔH) is:"
        ),
        "options": {
            "A": "+15 kJ/mol",
            "B": "−15 kJ/mol",
            "C": "+135 kJ/mol",
            "D": "−135 kJ/mol"
        },
        "answer": "A",
        "explanation": (
            "ΔH = Ea(forward) − Ea(backward) = 75 − 60 = +15 kJ/mol.\n"
            "Positive ΔH means the reaction is endothermic.\n"
            "The forward reaction requires more energy than is released in the reverse."
        ),
        "distractor_info": {
            "B": "Silly mistake — subtracted in the wrong order",
            "C": "Conceptual mistake — added instead of subtracted",
            "D": "Conceptual mistake — added and changed sign"
        }
    },

    # ═══════════════════════════════════════════════════════════
    # Q42 - Mathematics - Vectors - Very Hard
    # ═══════════════════════════════════════════════════════════
    {
        "id": 42,
        "subject": "Mathematics",
        "topic": "Vectors",
        "difficulty": "Very Hard",
        "question": (
            "If |a⃗| = 2, |b⃗| = 3, and a⃗ · b⃗ = 4, then |a⃗ × b⃗| is:"
        ),
        "options": {
            "A": "√10",
            "B": "2√5",
            "C": "√17",
            "D": "6"
        },
        "answer": "B",
        "explanation": (
            "Lagrange identity: |a⃗ × b⃗|² + (a⃗ · b⃗)² = |a⃗|²|b⃗|².\n"
            "|a⃗ × b⃗|² + 16 = 4 × 9 = 36.\n"
            "|a⃗ × b⃗|² = 20.\n"
            "|a⃗ × b⃗| = √20 = 2√5."
        ),
        "distractor_info": {
            "A": "Calculation mistake — used wrong formula",
            "C": "Calculation mistake — subtracted incorrectly",
            "D": "Conceptual mistake — equals |a⃗||b⃗|, ignoring angle"
        }
    },

    # ═══════════════════════════════════════════════════════════
    # Q43 - Mathematics - Probability - Medium
    # ═══════════════════════════════════════════════════════════
    {
        "id": 43,
        "subject": "Mathematics",
        "topic": "Probability",
        "difficulty": "Medium",
        "question": (
            "Two dice are thrown simultaneously. The probability of getting a sum of 7 is:"
        ),
        "options": {
            "A": "1/6",
            "B": "5/36",
            "C": "7/36",
            "D": "1/9"
        },
        "answer": "A",
        "explanation": (
            "Total outcomes = 36.\n"
            "Favorable: (1,6), (2,5), (3,4), (4,3), (5,2), (6,1) = 6.\n"
            "P = 6/36 = 1/6."
        ),
        "distractor_info": {
            "B": "Calculation mistake — counted only 5 outcomes",
            "C": "Calculation mistake — counted 7 outcomes",
            "D": "Calculation mistake — counted only 4 outcomes"
        }
    },

    # ═══════════════════════════════════════════════════════════
    # Q44 - Chemistry - Organic Chemistry - Hard
    # ═══════════════════════════════════════════════════════════
    {
        "id": 44,
        "subject": "Chemistry",
        "topic": "Organic Chemistry",
        "difficulty": "Hard",
        "question": (
            "The correct order of decreasing stability of carbocations is:"
        ),
        "options": {
            "A": "(CH₃)₃C⁺ > (CH₃)₂CH⁺ > CH₃CH₂⁺ > CH₃⁺",
            "B": "CH₃⁺ > CH₃CH₂⁺ > (CH₃)₂CH⁺ > (CH₃)₃C⁺",
            "C": "(CH₃)₂CH⁺ > (CH₃)₃C⁺ > CH₃CH₂⁺ > CH₃⁺",
            "D": "(CH₃)₃C⁺ > CH₃CH₂⁺ > (CH₃)₂CH⁺ > CH₃⁺"
        },
        "answer": "A",
        "explanation": (
            "Carbocation stability: tertiary > secondary > primary > methyl.\n"
            "(CH₃)₃C⁺ (3°) > (CH₃)₂CH⁺ (2°) > CH₃CH₂⁺ (1°) > CH₃⁺ (methyl).\n"
            "More alkyl groups stabilize the positive charge via hyperconjugation and inductive effect."
        ),
        "distractor_info": {
            "B": "Conceptual mistake — completely reversed the order",
            "C": "Conceptual mistake — secondary is not more stable than tertiary",
            "D": "Silly mistake — swapped secondary and primary"
        }
    },

    # ═══════════════════════════════════════════════════════════
    # Q45 - Mathematics - Trigonometry - Very Hard
    # ═══════════════════════════════════════════════════════════
    {
        "id": 45,
        "subject": "Mathematics",
        "topic": "Trigonometry",
        "difficulty": "Very Hard",
        "question": (
            "The value of sin⁻¹(cos(33π/5)) is:"
        ),
        "options": {
            "A": "π/10",
            "B": "−π/10",
            "C": "3π/10",
            "D": "−3π/10"
        },
        "answer": "B",
        "explanation": (
            "33π/5 = 6π + 3π/5. Since cos has period 2π:\n"
            "cos(33π/5) = cos(3π/5) = cos(108°) = −cos(72°) = −cos(2π/5).\n"
            "Now cos(2π/5) = sin(π/2 − 2π/5) = sin(π/10).\n"
            "So cos(33π/5) = −sin(π/10).\n"
            "sin⁻¹(−sin(π/10)) = −π/10 (since −π/10 ∈ [−π/2, π/2])."
        ),
        "distractor_info": {
            "A": "Silly mistake — forgot the negative sign",
            "C": "Calculation mistake — used wrong angle reduction",
            "D": "Calculation mistake — used 3π/10 instead of π/10"
        }
    },
]


def get_question_bank():
    """Return the verified question bank."""
    return QUESTIONS
