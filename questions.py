"""
PCM Advanced Mock Test - Question Bank
=======================================
45 Questions organized strictly into 3 sequential sections:
- SECTION 1: Physics (Questions 1 to 16)
- SECTION 2: Chemistry (Questions 17 to 32)
- SECTION 3: Mathematics (Questions 33 to 45, featuring 11 Trigonometry questions)
"""

QUESTIONS = [
    # ═══════════════════════════════════════════════════════════
    # SECTION 1: PHYSICS (Questions 1 to 16)
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
    {
        "id": 2,
        "subject": "Physics",
        "topic": "Electrostatics",
        "difficulty": "Hard",
        "question": (
            "A uniformly charged thin ring of radius R has total charge Q. A point charge q is placed "
            "on the axis of the ring at a distance x = R from the centre. The magnitude of the electrostatic force on q is:"
        ),
        "options": {
            "A": "Qq / (4π ε₀ R² 2√2)",
            "B": "Qq / (4π ε₀ R² √2)",
            "C": "Qq / (4π ε₀ R²)",
            "D": "Qq / (8π ε₀ R²)"
        },
        "answer": "A",
        "explanation": (
            "Electric field on the axis of a thin ring: E = (k Q x) / (R² + x²)^(3/2).\n"
            "Substitute x = R:\n"
            "E = (k Q R) / (R² + R²)^(3/2) = (k Q R) / (2R²)^(3/2) = (k Q R) / (2√2 R³) = k Q / (2√2 R²).\n"
            "Force F = q E = Qq / (4π ε₀ R² 2√2)."
        ),
        "distractor_info": {
            "B": "Calculation mistake — forgot factor of 2 in (2)^(3/2)",
            "C": "Formula mistake — used point charge formula kQq/R²",
            "D": "Calculation mistake — used 2R³ instead of 2√2 R³"
        }
    },
    {
        "id": 3,
        "subject": "Physics",
        "topic": "Electrostatics",
        "difficulty": "Hard",
        "question": (
            "Four point charges +q, −q, +q, −q are placed at the vertices A, B, C, D of a square of side a "
            "in order. The electric potential at the centre O of the square is:"
        ),
        "options": {
            "A": "0",
            "B": "4kq / (a √2)",
            "C": "2kq / a",
            "D": "2√2 kq / a"
        },
        "answer": "A",
        "explanation": (
            "Distance from centre O to each vertex r = a / √2.\n"
            "Potential V_O = k(+q)/r + k(−q)/r + k(+q)/r + k(−q)/r = (k/r)(q − q + q − q) = 0."
        ),
        "distractor_info": {
            "B": "Conceptual mistake — added magnitudes ignoring signs",
            "C": "Formula mistake — used side length a instead of distance to centre",
            "D": "Calculation mistake — incorrect scalar addition"
        }
    },
    {
        "id": 4,
        "subject": "Physics",
        "topic": "Electrostatics",
        "difficulty": "Hard",
        "question": (
            "A point charge +q is located at the centre of a cube of side length L. "
            "The electric flux passing through one face of the cube is:"
        ),
        "options": {
            "A": "q / (6ε₀)",
            "B": "q / ε₀",
            "C": "q / (4ε₀)",
            "D": "q / (24ε₀)"
        },
        "answer": "A",
        "explanation": (
            "By Gauss's Law, the total electric flux passing through the entire closed surface of the cube is Φ_total = q / ε₀.\n"
            "By symmetry, the flux is distributed equally across all 6 identical faces of the cube.\n"
            "Therefore, the flux through one face = Φ_total / 6 = q / (6ε₀)."
        ),
        "distractor_info": {
            "B": "Conceptual mistake — gave total flux instead of flux per face",
            "C": "Formula mistake — confused cube faces (6) with tetrahedron faces (4)",
            "D": "Calculation mistake — multiplied by 4 instead of dividing by 6"
        }
    },
    {
        "id": 5,
        "subject": "Physics",
        "topic": "Electrostatics",
        "difficulty": "Hard",
        "question": (
            "A parallel plate capacitor with plate area A and separation d is charged to potential difference V "
            "and then disconnected from the battery. A dielectric slab of dielectric constant K = 4 and thickness d "
            "is inserted to completely fill the space between the plates. The ratio of initial to final stored electrostatic energy is:"
        ),
        "options": {
            "A": "4 : 1",
            "B": "1 : 4",
            "C": "1 : 16",
            "D": "16 : 1"
        },
        "answer": "A",
        "explanation": (
            "When disconnected from battery, charge Q remains constant.\n"
            "Initial capacitance C₀, initial energy U_i = Q² / (2C₀).\n"
            "After inserting slab of dielectric constant K, new capacitance C' = K C₀ = 4 C₀.\n"
            "Final energy U_f = Q² / (2 C') = Q² / (8 C₀) = U_i / 4.\n"
            "Ratio U_i / U_f = 4 / 1 = 4 : 1."
        ),
        "distractor_info": {
            "B": "Conceptual mistake — assumed voltage remains constant instead of charge",
            "C": "Formula mistake — squared K in energy calculation",
            "D": "Calculation mistake — inverted the initial and final states"
        }
    },
    {
        "id": 6,
        "subject": "Physics",
        "topic": "Electrostatics",
        "difficulty": "Very Hard",
        "question": (
            "A capacitor of capacitance C₁ = 2 μF is charged to V₁ = 100 V and disconnected. "
            "It is then connected in parallel with an uncharged capacitor C₂ = 3 μF. "
            "The electrostatic energy lost during the process is:"
        ),
        "options": {
            "A": "6.0 mJ",
            "B": "4.0 mJ",
            "C": "10.0 mJ",
            "D": "1.0 mJ"
        },
        "answer": "A",
        "explanation": (
            "Formula for energy loss when connecting two capacitors: ΔU = ½ [C₁ C₂ / (C₁ + C₂)] (V₁ − V₂)².\n"
            "Here C₁ = 2 μF, C₂ = 3 μF, V₁ = 100 V, V₂ = 0 V.\n"
            "ΔU = ½ × [(2 × 3) / (2 + 3)] × 10⁻⁶ × (100 − 0)²\n"
            "ΔU = ½ × (6 / 5) × 10⁻⁶ × 10000 = ½ × 1.2 × 10⁻² J = 0.6 × 10⁻² J = 6.0 × 10⁻³ J = 6.0 mJ."
        ),
        "distractor_info": {
            "B": "Calculation mistake — subtracted final stored energy from total initial without C₂ share",
            "C": "Conceptual mistake — gave initial stored energy",
            "D": "Formula mistake — missed factor of 1/2 in loss formula"
        }
    },
    {
        "id": 7,
        "subject": "Physics",
        "topic": "Current Electricity",
        "difficulty": "Hard",
        "question": (
            "A copper wire of cross-sectional area 1.0 mm² carries a steady current of 4.8 A. "
            "If the number density of free electrons in copper is 8.5 × 10²⁸ m⁻³, "
            "the drift velocity of free electrons is approximately (e = 1.6 × 10⁻¹⁹ C):"
        ),
        "options": {
            "A": "0.35 mm/s",
            "B": "3.5 mm/s",
            "C": "0.035 mm/s",
            "D": "35 mm/s"
        },
        "answer": "A",
        "explanation": (
            "Current I = n A e v_d  =>  v_d = I / (n A e).\n"
            "I = 4.8 A, A = 1.0 × 10⁻⁶ m², n = 8.5 × 10²⁸ m⁻³, e = 1.6 × 10⁻¹⁹ C.\n"
            "Denominator = 8.5 × 10²⁸ × 1.0 × 10⁻⁶ × 1.6 × 10⁻¹⁹ = 8.5 × 1.6 × 10³ = 13.6 × 10³ = 13600.\n"
            "v_d = 4.8 / 13600 = 3.53 × 10⁻⁴ m/s = 0.353 mm/s."
        ),
        "distractor_info": {
            "B": "Calculation mistake — power of 10 error converting m² to mm²",
            "C": "Calculation mistake — divided by 10",
            "D": "Unit conversion error — multiplied by 100"
        }
    },
    {
        "id": 8,
        "subject": "Physics",
        "topic": "Current Electricity",
        "difficulty": "Hard",
        "question": (
            "The resistance of a conductor is 10 Ω at 20°C and 12 Ω at 70°C. "
            "The temperature coefficient of resistance α of the material is:"
        ),
        "options": {
            "A": "0.004 °C⁻¹",
            "B": "0.002 °C⁻¹",
            "C": "0.04 °C⁻¹",
            "D": "0.008 °C⁻¹"
        },
        "answer": "A",
        "explanation": (
            "Formula: R_T = R₀(1 + α ΔT).\n"
            "R₇₀ - R₂₀ = R₂₀ α (70 - 20)  =>  12 - 10 = 10 × α × 50.\n"
            "2 = 500 α  =>  α = 2 / 500 = 0.004 °C⁻¹."
        ),
        "distractor_info": {
            "B": "Calculation mistake — used 100°C temperature difference",
            "C": "Decimal mistake — misplaced decimal point",
            "D": "Formula mistake — used 12 Ω as reference resistance R₀"
        }
    },
    {
        "id": 9,
        "subject": "Physics",
        "topic": "Current Electricity",
        "difficulty": "Hard",
        "question": (
            "In a Wheatstone bridge, four resistances P = 10 Ω, Q = 20 Ω, R = 30 Ω, and S = 60 Ω "
            "are connected in order. A galvanometer of resistance 50 Ω is connected across the bridge. "
            "The current through the galvanometer is:"
        ),
        "options": {
            "A": "0",
            "B": "0.1 A",
            "C": "0.05 A",
            "D": "0.2 A"
        },
        "answer": "A",
        "explanation": (
            "Check condition for balanced Wheatstone bridge: P / Q = R / S.\n"
            "P/Q = 10/20 = 1/2. R/S = 30/60 = 1/2.\n"
            "Since P/Q = R/S, the bridge is balanced. Potential difference across the galvanometer branch is ZERO.\n"
            "Therefore, current through the galvanometer is 0."
        ),
        "distractor_info": {
            "B": "Calculation mistake — tried calculating current assuming unbalanced bridge",
            "C": "Formula mistake — divided voltage by galvanometer resistance directly",
            "D": "Conceptual mistake — failed to check balance condition"
        }
    },
    {
        "id": 10,
        "subject": "Physics",
        "topic": "Current Electricity",
        "difficulty": "Hard",
        "question": (
            "A potentiometer wire of length 10 m and resistance 20 Ω is connected in series with a 3 V battery "
            "and an external resistance of 10 Ω. The potential gradient along the potentiometer wire is:"
        ),
        "options": {
            "A": "0.2 V/m",
            "B": "0.3 V/m",
            "C": "0.1 V/m",
            "D": "0.5 V/m"
        },
        "answer": "A",
        "explanation": (
            "Total circuit resistance R_total = R_wire + R_ext = 20 + 10 = 30 Ω.\n"
            "Circuit current I = V / R_total = 3 V / 30 Ω = 0.1 A.\n"
            "Potential drop across potentiometer wire V_wire = I × R_wire = 0.1 A × 20 Ω = 2 V.\n"
            "Potential gradient k = V_wire / L = 2 V / 10 m = 0.2 V/m."
        ),
        "distractor_info": {
            "B": "Formula mistake — used total voltage (3V) directly without subtracting external drop",
            "C": "Calculation mistake — divided by 20m instead of 10m",
            "D": "Conceptual mistake — ignored external resistance"
        }
    },
    {
        "id": 11,
        "subject": "Physics",
        "topic": "Moving Charges & Magnetism",
        "difficulty": "Hard",
        "question": (
            "A circular loop of radius R carries a current I. The magnetic field at its centre is B₁. "
            "The magnetic field at a point on its axis at a distance x = R from the centre is B₂. "
            "The ratio B₁ : B₂ is:"
        ),
        "options": {
            "A": "2√2 : 1",
            "B": "2 : 1",
            "C": "√2 : 1",
            "D": "4 : 1"
        },
        "answer": "A",
        "explanation": (
            "Field at centre: B₁ = μ₀ I / (2R).\n"
            "Field on axis: B₂ = μ₀ I R² / [2(R² + x²)^(3/2)].\n"
            "For x = R: B₂ = μ₀ I R² / [2(2R²)^(3/2)] = μ₀ I R² / [2 × 2√2 R³] = μ₀ I / (4√2 R).\n"
            "Ratio B₁ / B₂ = [μ₀ I / (2R)] / [μ₀ I / (4√2 R)] = (4√2) / 2 = 2√2.\n"
            "B₁ : B₂ = 2√2 : 1."
        ),
        "distractor_info": {
            "B": "Calculation mistake — forgot (2)^(3/2) = 2√2",
            "C": "Calculation mistake — square rooted the ratio",
            "D": "Formula mistake — assumed inverse square law with distance"
        }
    },
    {
        "id": 12,
        "subject": "Physics",
        "topic": "Moving Charges & Magnetism",
        "difficulty": "Very Hard",
        "question": (
            "An electron moving with velocity v = 3 × 10⁶ m/s enters a region of uniform magnetic field "
            "B = 0.2 T at an angle of 30° to the magnetic field lines. "
            "The pitch of the helical path followed by the electron is (m_e = 9.1 × 10⁻³¹ kg, e = 1.6 × 10⁻¹⁹ C):"
        ),
        "options": {
            "A": "0.46 mm",
            "B": "0.27 mm",
            "C": "0.53 mm",
            "D": "0.92 mm"
        },
        "answer": "A",
        "explanation": (
            "Component of velocity parallel to field: v_|| = v cos 30° = 3 × 10⁶ × (√3/2) = 2.598 × 10⁶ m/s.\n"
            "Time period of one helical revolution: T = 2π m / (e B).\n"
            "T = (2 × 3.1416 × 9.1 × 10⁻³¹) / (1.6 × 10⁻¹⁹ × 0.2) = 5.718 × 10⁻³⁰ / 3.2 × 10⁻²⁰ = 1.787 × 10⁻¹⁰ s.\n"
            "Pitch = v_|| × T = 2.598 × 10⁶ × 1.787 × 10⁻¹⁰ = 4.64 × 10⁻⁴ m = 0.464 mm."
        ),
        "distractor_info": {
            "B": "Formula mistake — used v sin 30° instead of v cos 30°",
            "C": "Calculation mistake — used total velocity v instead of parallel component v_||",
            "D": "Calculation mistake — doubled the time period"
        }
    },
    {
        "id": 13,
        "subject": "Physics",
        "topic": "Moving Charges & Magnetism",
        "difficulty": "Hard",
        "question": (
            "A long straight wire carries a current of 35 A. The magnitude of magnetic field B "
            "at a point 20 cm from the wire is:"
        ),
        "options": {
            "A": "3.5 × 10⁻⁵ T",
            "B": "3.5 × 10⁻⁴ T",
            "C": "1.75 × 10⁻⁵ T",
            "D": "7.0 × 10⁻⁵ T"
        },
        "answer": "A",
        "explanation": (
            "Magnetic field of long straight wire: B = (μ₀ I) / (2π r).\n"
            "Here I = 35 A, r = 0.20 m, μ₀ / (2π) = 2 × 10⁻⁷ T·m/A.\n"
            "B = (2 × 10⁻⁷ × 35) / 0.20 = 70 × 10⁻⁷ / 0.20 = 350 × 10⁻⁷ = 3.5 × 10⁻⁵ T."
        ),
        "distractor_info": {
            "B": "Unit conversion error — used 20 m instead of 0.2 m",
            "C": "Formula mistake — used 4π in denominator instead of 2π",
            "D": "Calculation mistake — multiplied by 2"
        }
    },
    {
        "id": 14,
        "subject": "Physics",
        "topic": "Moving Charges & Magnetism",
        "difficulty": "Hard",
        "question": (
            "A square coil of side 10 cm consists of 20 turns and carries a current of 12 A. "
            "The coil is suspended vertically and the normal to the plane of the coil makes an angle of 30° "
            "with the direction of a uniform horizontal magnetic field of magnitude 0.80 T. "
            "The torque experienced by the coil is:"
        ),
        "options": {
            "A": "0.96 N·m",
            "B": "1.66 N·m",
            "C": "1.92 N·m",
            "D": "0.48 N·m"
        },
        "answer": "A",
        "explanation": (
            "Torque τ = N I A B sin θ.\n"
            "N = 20, I = 12 A, A = (0.10 m)² = 0.01 m², B = 0.80 T, θ = 30°.\n"
            "Magnetic dipole moment M = N I A = 20 × 12 × 0.01 = 2.4 A·m².\n"
            "τ = M B sin 30° = 2.4 × 0.80 × 0.5 = 0.96 N·m."
        ),
        "distractor_info": {
            "B": "Formula mistake — used cos 30° instead of sin 30°",
            "C": "Formula mistake — omitted sin 30° (assumed θ = 90°)",
            "D": "Calculation mistake — omitted factor of N (turns)"
        }
    },
    {
        "id": 15,
        "subject": "Physics",
        "topic": "Moving Charges & Magnetism",
        "difficulty": "Hard",
        "question": (
            "A galvanometer of resistance 15 Ω gives full scale deflection for a current of 4 mA. "
            "To convert it into a voltmeter of range 0 – 18 V, the resistance to be connected in series with the galvanometer is:"
        ),
        "options": {
            "A": "4485 Ω",
            "B": "4500 Ω",
            "C": "4515 Ω",
            "D": "4470 Ω"
        },
        "answer": "A",
        "explanation": (
            "Voltmeter formula: V = I_g (G + R_s)  =>  R_s = (V / I_g) − G.\n"
            "Here V = 18 V, I_g = 4 mA = 4 × 10⁻³ A, G = 15 Ω.\n"
            "V / I_g = 18 / (4 × 10⁻³) = 18000 / 4 = 4500 Ω.\n"
            "R_s = 4500 − 15 = 4485 Ω."
        ),
        "distractor_info": {
            "B": "Formula mistake — forgot to subtract galvanometer resistance G",
            "C": "Calculation mistake — added G instead of subtracting",
            "D": "Calculation mistake — subtracted 30 Ω"
        }
    },
    {
        "id": 16,
        "subject": "Physics",
        "topic": "Moving Charges & Magnetism",
        "difficulty": "Hard",
        "question": (
            "A solenoid of length 0.5 m and radius 1 cm has 500 turns. It carries a current of 5 A. "
            "The magnetic field inside the solenoid near its centre is (μ₀ = 4π × 10⁻⁷ T·m/A):"
        ),
        "options": {
            "A": "6.28 × 10⁻³ T",
            "B": "3.14 × 10⁻³ T",
            "C": "1.26 × 10⁻² T",
            "D": "6.28 × 10⁻⁴ T"
        },
        "answer": "A",
        "explanation": (
            "Magnetic field inside a solenoid: B = μ₀ n I = μ₀ (N / L) I.\n"
            "N = 500, L = 0.5 m  =>  n = 500 / 0.5 = 1000 turns/m.\n"
            "I = 5 A, μ₀ = 4π × 10⁻⁷ = 1.2566 × 10⁻⁶ T·m/A.\n"
            "B = 4π × 10⁻⁷ × 1000 × 5 = 20000 π × 10⁻⁷ = 2π × 10⁻³ T = 6.283 × 10⁻³ T."
        ),
        "distractor_info": {
            "B": "Formula mistake — used field at the end of solenoid B = ½ μ₀ n I",
            "C": "Calculation mistake — multiplied by 2",
            "D": "Decimal mistake — miscalculated number of turns per metre"
        }
    },

    # ═══════════════════════════════════════════════════════════
    # SECTION 2: CHEMISTRY (Questions 17 to 32)
    # ═══════════════════════════════════════════════════════════
    {
        "id": 17,
        "subject": "Chemistry",
        "topic": "Chemical Kinetics",
        "difficulty": "Hard",
        "question": (
            "For a reaction A + 2B → Products, the following data is obtained:\n\n"
            "Expt 1: [A]₀ = 0.10 M, [B]₀ = 0.10 M, Rate = 2.0 × 10⁻³ M/s\n"
            "Expt 2: [A]₀ = 0.20 M, [B]₀ = 0.10 M, Rate = 8.0 × 10⁻³ M/s\n"
            "Expt 3: [A]₀ = 0.20 M, [B]₀ = 0.20 M, Rate = 8.0 × 10⁻³ M/s\n\n"
            "The rate law for the reaction is:"
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
            "Rate = k[A]². Stoichiometric coefficients do NOT determine rate law."
        ),
        "distractor_info": {
            "A": "Conceptual mistake — assumed B participates based on stoichiometry",
            "C": "Conceptual mistake — confused orders of A and B",
            "D": "Conceptual mistake — assumed order equals stoichiometric coefficient for both"
        }
    },
    {
        "id": 18,
        "subject": "Chemistry",
        "topic": "Chemical Kinetics",
        "difficulty": "Hard",
        "question": (
            "The half-life of a first-order reaction is 30 minutes. "
            "The time required for 75% completion of the reaction is:"
        ),
        "options": {
            "A": "60 min",
            "B": "45 min",
            "C": "90 min",
            "D": "120 min"
        },
        "answer": "A",
        "explanation": (
            "For a first-order reaction, the time required for 75% completion is t_75% = 2 × t_1/2.\n"
            "Given t_1/2 = 30 minutes.\n"
            "t_75% = 2 × 30 min = 60 minutes."
        ),
        "distractor_info": {
            "B": "Calculation mistake — assumed linear relationship (1.5 × 30)",
            "C": "Formula mistake — used 3 half-lives",
            "D": "Calculation mistake — used 4 half-lives"
        }
    },
    {
        "id": 19,
        "subject": "Chemistry",
        "topic": "Chemical Kinetics",
        "difficulty": "Very Hard",
        "question": (
            "For a first-order reaction A → B, the rate constant k = 6.93 × 10⁻³ min⁻¹. "
            "If the initial concentration of A is 0.10 M, the concentration of A remaining after 100 minutes is:"
        ),
        "options": {
            "A": "0.05 M",
            "B": "0.025 M",
            "C": "0.01 M",
            "D": "0.075 M"
        },
        "answer": "A",
        "explanation": (
            "First find half-life: t_1/2 = 0.693 / k = 0.693 / (6.93 × 10⁻³) = 100 minutes.\n"
            "Since the elapsed time is 100 minutes, exactly ONE half-life has passed.\n"
            "Concentration remaining [A] = [A]₀ / 2 = 0.10 M / 2 = 0.05 M."
        ),
        "distractor_info": {
            "B": "Calculation mistake — assumed 2 half-lives passed",
            "C": "Formula mistake — incorrect exponential evaluation",
            "D": "Calculation mistake — subtracted rate constant from initial concentration"
        }
    },
    {
        "id": 20,
        "subject": "Chemistry",
        "topic": "Chemical Kinetics",
        "difficulty": "Hard",
        "question": (
            "The activation energy of a chemical reaction is 50 kJ/mol. "
            "If the rate constant doubles when the temperature increases from 300 K to 310 K, "
            "what is the approximate value of the gas constant R used in the Arrhenius equation?"
        ),
        "options": {
            "A": "8.314 J/(mol·K)",
            "B": "1.987 cal/(mol·K)",
            "C": "0.0821 L·atm/(mol·K)",
            "D": "6.022 × 10²³ J/(mol·K)"
        },
        "answer": "A",
        "explanation": (
            "In SI units, activation energy E_a is in Joules (50,000 J/mol).\n"
            "The gas constant R in SI units is 8.314 J/(mol·K).\n"
            "Arrhenius equation: ln(k₂/k₁) = (E_a / R) × (1/T₁ − 1/T₂)."
        ),
        "distractor_info": {
            "B": "Unit confusion — calorie unit instead of Joules",
            "C": "Unit confusion — L·atm unit used for ideal gas law",
            "D": "Conceptual mistake — confused gas constant with Avogadro's number"
        }
    },
    {
        "id": 21,
        "subject": "Chemistry",
        "topic": "Chemical Kinetics",
        "difficulty": "Hard",
        "question": (
            "Acid hydrolysis of ethyl acetate is an example of:"
        ),
        "options": {
            "A": "Pseudo-first-order reaction",
            "B": "Second-order reaction",
            "C": "Zero-order reaction",
            "D": "Third-order reaction"
        },
        "answer": "A",
        "explanation": (
            "Acid hydrolysis of ester: CH₃COOCH₂CH₃ + H₂O --(H⁺)--> CH₃COOH + CH₃CH₂OH.\n"
            "Water is present in large excess, so its concentration remains essentially constant throughout the reaction.\n"
            "Thus, rate = k'[CH₃COOCH₂CH₃][H₂O] = k[CH₃COOCH₂CH₃], making it a pseudo-first-order reaction."
        ),
        "distractor_info": {
            "B": "Conceptual mistake — counted both reactants ignoring excess water",
            "C": "Conceptual mistake — confused with enzyme kinetics at saturation",
            "D": "Formula mistake — miscounted molecularity as order"
        }
    },
    {
        "id": 22,
        "subject": "Chemistry",
        "topic": "Chemical Kinetics",
        "difficulty": "Hard",
        "question": (
            "The unit of rate constant for a zero-order reaction is:"
        ),
        "options": {
            "A": "mol L⁻¹ s⁻¹",
            "B": "s⁻¹",
            "C": "L mol⁻¹ s⁻¹",
            "D": "L² mol⁻² s⁻¹"
        },
        "answer": "A",
        "explanation": (
            "General unit of rate constant k = (mol L⁻¹)^(1−n) s⁻¹, where n is the order of reaction.\n"
            "For n = 0: k = (mol L⁻¹)^(1−0) s⁻¹ = mol L⁻¹ s⁻¹."
        ),
        "distractor_info": {
            "B": "Confused with first-order rate constant unit",
            "C": "Confused with second-order rate constant unit",
            "D": "Confused with third-order rate constant unit"
        }
    },
    {
        "id": 23,
        "subject": "Chemistry",
        "topic": "Solid State",
        "difficulty": "Hard",
        "question": (
            "An element with molar mass 60 g/mol crystallises in a face-centred cubic (fcc) lattice "
            "with edge length a = 400 pm. The density of the crystal is (N_A = 6.022 × 10²³ mol⁻¹):"
        ),
        "options": {
            "A": "6.23 g/cm³",
            "B": "3.12 g/cm³",
            "C": "1.56 g/cm³",
            "D": "12.45 g/cm³"
        },
        "answer": "A",
        "explanation": (
            "Density formula ρ = (Z × M) / (a³ × N_A).\n"
            "For fcc lattice, Z = 4. M = 60 g/mol.\n"
            "Edge length a = 400 pm = 400 × 10⁻¹⁰ cm = 4 × 10⁻⁸ cm.\n"
            "a³ = (4 × 10⁻⁸)³ = 64 × 10⁻²⁴ cm³.\n"
            "ρ = (4 × 60) / (64 × 10⁻²⁴ × 6.022 × 10²³) = 240 / (38.54) = 6.227 g/cm³ ≈ 6.23 g/cm³."
        ),
        "distractor_info": {
            "B": "Calculation mistake — used Z = 2 (bcc) instead of Z = 4 (fcc)",
            "C": "Calculation mistake — used Z = 1 (simple cubic)",
            "D": "Calculation mistake — doubled Z"
        }
    },
    {
        "id": 24,
        "subject": "Chemistry",
        "topic": "Solid State",
        "difficulty": "Hard",
        "question": (
            "The packing efficiency of face-centred cubic (fcc), body-centred cubic (bcc), "
            "and simple cubic (sc) unit cells are respectively:"
        ),
        "options": {
            "A": "74%, 68%, 52.4%",
            "B": "68%, 74%, 52.4%",
            "C": "74%, 52.4%, 68%",
            "D": "52.4%, 68%, 74%"
        },
        "answer": "A",
        "explanation": (
            "Packing efficiency:\n"
            "- fcc (or hcp) = 74%\n"
            "- bcc = 68%\n"
            "- simple cubic (sc) = 52.4%\n"
            "Thus the order fcc, bcc, sc is 74%, 68%, 52.4%."
        ),
        "distractor_info": {
            "B": "Swapped fcc and bcc values",
            "C": "Swapped bcc and simple cubic values",
            "D": "Reversed the order"
        }
    },
    {
        "id": 25,
        "subject": "Chemistry",
        "topic": "Solid State",
        "difficulty": "Hard",
        "question": (
            "Schottky defect in a crystal is observed when:"
        ),
        "options": {
            "A": "Equal number of cations and anions are missing from lattice sites",
            "B": "An ion leaves its lattice site and occupies an interstitial position",
            "C": "Density of the crystal increases",
            "D": "Impurity ions occupy lattice sites"
        },
        "answer": "A",
        "explanation": (
            "Schottky defect is a vacancy defect in ionic solids where equal numbers of cations "
            "and anions are missing from their lattice sites, maintaining electrical neutrality "
            "and decreasing the overall density of the crystal."
        ),
        "distractor_info": {
            "B": "Confused with Frenkel defect definition",
            "C": "Factual error — Schottky defect decreases density",
            "D": "Confused with interstitial impurity defect"
        }
    },
    {
        "id": 26,
        "subject": "Chemistry",
        "topic": "Solid State",
        "difficulty": "Hard",
        "question": (
            "In a face-centred cubic (fcc) unit cell, the relation between atomic radius r and edge length a is:"
        ),
        "options": {
            "A": "r = a / (2√2)",
            "B": "r = (√3 a) / 4",
            "C": "r = a / 2",
            "D": "r = √2 a"
        },
        "answer": "A",
        "explanation": (
            "In fcc, atoms touch along the face diagonal.\n"
            "Face diagonal length = √2 a = 4r  =>  r = (√2 a) / 4 = a / (2√2)."
        ),
        "distractor_info": {
            "B": "Confused with bcc formula r = (√3 a) / 4",
            "C": "Confused with simple cubic formula r = a / 2",
            "D": "Calculation mistake — inverted relationship"
        }
    },
    {
        "id": 27,
        "subject": "Chemistry",
        "topic": "Solutions",
        "difficulty": "Hard",
        "question": (
            "A solution containing 6.0 g of a non-volatile solute in 180 g of water has a vapour pressure "
            "of 23.50 mmHg at 25°C. Pure water has a vapour pressure of 23.75 mmHg at 25°C. "
            "The molar mass of the solute is:"
        ),
        "options": {
            "A": "60 g/mol",
            "B": "180 g/mol",
            "C": "120 g/mol",
            "D": "90 g/mol"
        },
        "answer": "A",
        "explanation": (
            "By Raoult's Law: (P⁰ − P) / P⁰ = x_solute = n_solute / (n_solute + n_solvent) ≈ n_solute / n_solvent (for dilute solution).\n"
            "(23.75 − 23.50) / 23.75 = 0.25 / 23.75 = 1 / 95.\n"
            "n_solvent = 180 / 18 = 10 mol.\n"
            "n_solute / 10 = 1 / 95  =>  n_solute = 10 / 95 ≈ 0.105 mol.\n"
            "Molar mass = 6.0 g / 0.10 mol = 60 g/mol."
        ),
        "distractor_info": {
            "B": "Calculation mistake — used solvent molar mass directly",
            "C": "Calculation mistake — doubled the answer",
            "D": "Formula mistake — used total mass"
        }
    },
    {
        "id": 28,
        "subject": "Chemistry",
        "topic": "Solutions",
        "difficulty": "Hard",
        "question": (
            "The freezing point of a 0.1 m aqueous solution of a non-electrolyte solute is (K_f of water = 1.86 K kg/mol):"
        ),
        "options": {
            "A": "−0.186 °C",
            "B": "+0.186 °C",
            "C": "−0.372 °C",
            "D": "−1.86 °C"
        },
        "answer": "A",
        "explanation": (
            "Depression in freezing point ΔT_f = i × K_f × m.\n"
            "For non-electrolyte, i = 1.\n"
            "ΔT_f = 1 × 1.86 × 0.1 = 0.186 K.\n"
            "Freezing point of solution T_f = T_f° − ΔT_f = 0 °C − 0.186 °C = −0.186 °C."
        ),
        "distractor_info": {
            "B": "Conceptual mistake — gave positive value instead of sub-zero freezing point",
            "C": "Formula mistake — used van 't Hoff factor i = 2",
            "D": "Calculation mistake — used m = 1.0 instead of 0.1"
        }
    },
    {
        "id": 29,
        "subject": "Chemistry",
        "topic": "Solutions",
        "difficulty": "Hard",
        "question": (
            "Which of the following colligative properties is best suited for the determination "
            "of molar mass of macromolecules like proteins and polymers?"
        ),
        "options": {
            "A": "Osmotic pressure",
            "B": "Elevation in boiling point",
            "C": "Depression in freezing point",
            "D": "Relative lowering of vapour pressure"
        },
        "answer": "A",
        "explanation": (
            "Osmotic pressure measurement is preferred for macromolecules because:\n"
            "1. It is measured around room temperature (preventing protein denaturation).\n"
            "2. Its magnitude is significantly larger and easily measurable even for extremely dilute solutions."
        ),
        "distractor_info": {
            "B": "High temperature causes thermal degradation of proteins",
            "C": "Freezing point changes are too small to measure accurately for macromolecules",
            "D": "Vapour pressure changes are negligibly small for macromolecule solutions"
        }
    },
    {
        "id": 30,
        "subject": "Chemistry",
        "topic": "Solutions",
        "difficulty": "Hard",
        "question": (
            "The van 't Hoff factor (i) for a completely dissociated BaCl₂ solution is:"
        ),
        "options": {
            "A": "3",
            "B": "2",
            "C": "1",
            "D": "4"
        },
        "answer": "A",
        "explanation": (
            "Barium chloride dissociates in water: BaCl₂ → Ba²⁺ + 2 Cl⁻.\n"
            "Total number of ions produced per formula unit = 1 + 2 = 3.\n"
            "For 100% dissociation, van 't Hoff factor i = 3."
        ),
        "distractor_info": {
            "B": "Calculated for binary salt like NaCl",
            "C": "Calculated for non-electrolyte",
            "D": "Counted 1 Ba, 2 Cl, plus 1 original molecule"
        }
    },
    {
        "id": 31,
        "subject": "Chemistry",
        "topic": "Solutions",
        "difficulty": "Hard",
        "question": (
            "Two solutions A and B are separated by a semipermeable membrane. "
            "If solvent flows from solution A to solution B, then:"
        ),
        "options": {
            "A": "Solution A is hypotonic relative to Solution B",
            "B": "Solution A is hypertonic relative to Solution B",
            "C": "Both solutions are isotonic",
            "D": "Solution B has lower osmotic pressure than A"
        },
        "answer": "A",
        "explanation": (
            "Solvent flows spontaneously from lower solute concentration (hypotonic) "
            "to higher solute concentration (hypertonic) through a semipermeable membrane. "
            "Hence Solution A has lower concentration (hypotonic) compared to B."
        ),
        "distractor_info": {
            "B": "Reversed the direction of solvent flow",
            "C": "No net flow occurs between isotonic solutions",
            "D": "Solution B has higher osmotic pressure, not lower"
        }
    },
    {
        "id": 32,
        "subject": "Chemistry",
        "topic": "Solutions",
        "difficulty": "Very Hard",
        "question": (
            "An ideal solution is formed by mixing two liquids A and B. Which of the following conditions is TRUE?"
        ),
        "options": {
            "A": "Δ_mix H = 0, Δ_mix V = 0",
            "B": "Δ_mix H > 0, Δ_mix V > 0",
            "C": "Δ_mix H < 0, Δ_mix V < 0",
            "D": "Δ_mix H = 0, Δ_mix S = 0"
        },
        "answer": "A",
        "explanation": (
            "For an ideal solution obeying Raoult's law over the entire concentration range:\n"
            "1. Enthalpy of mixing Δ_mix H = 0 (no heat evolved or absorbed).\n"
            "2. Volume change of mixing Δ_mix V = 0 (no expansion or contraction).\n"
            "Note: Entropy of mixing Δ_mix S is always > 0 for mixing."
        ),
        "distractor_info": {
            "B": "Describes positive deviation from Raoult's law",
            "C": "Describes negative deviation from Raoult's law",
            "D": "Incorrect — entropy of mixing Δ_mix S is always positive (> 0)"
        }
    },

    # ═══════════════════════════════════════════════════════════
    # SECTION 3: MATHEMATICS (Questions 33 to 45)
    # Featuring 11 High-Yield Trigonometry Questions!
    # ═══════════════════════════════════════════════════════════
    {
        "id": 33,
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
            "B": "Calculation mistake — error expanding the cubic expression",
            "C": "Calculation mistake — squared instead of cubed",
            "D": "Conceptual mistake — incorrect substitution"
        }
    },
    {
        "id": 34,
        "subject": "Mathematics",
        "topic": "Trigonometry",
        "difficulty": "Hard",
        "question": (
            "The number of solutions of the trigonometric equation sin x + cos x = 1 in the interval [0, 2π] is:"
        ),
        "options": {
            "A": "3",
            "B": "2",
            "C": "1",
            "D": "4"
        },
        "answer": "A",
        "explanation": (
            "Divide by √2: (1/√2) sin x + (1/√2) cos x = 1 / √2.\n"
            "sin(x + π/4) = 1 / √2 = sin(π/4).\n"
            "In [0, 2π], x + π/4 can take values:\n"
            "1. x + π/4 = π/4  =>  x = 0\n"
            "2. x + π/4 = 3π/4  =>  x = π/2\n"
            "3. x + π/4 = 9π/4  =>  x = 2π\n"
            "All three values x = 0, π/2, 2π lie within [0, 2π].\n"
            "Hence there are 3 solutions."
        ),
        "distractor_info": {
            "B": "Missed the boundary solution x = 2π",
            "C": "Only found x = 0",
            "D": "Included an out-of-interval solution"
        }
    },
    {
        "id": 35,
        "subject": "Mathematics",
        "topic": "Trigonometry",
        "difficulty": "Hard",
        "question": (
            "The maximum value of the function f(x) = 3 sin x + 4 cos x + 5 is:"
        ),
        "options": {
            "A": "10",
            "B": "12",
            "C": "7",
            "D": "5"
        },
        "answer": "A",
        "explanation": (
            "The expression a sin x + b cos x has maximum value √(a² + b²).\n"
            "Here a = 3, b = 4  =>  √(3² + 4²) = √(9 + 16) = √25 = 5.\n"
            "Maximum value of f(x) = 5 + 5 = 10."
        ),
        "distractor_info": {
            "B": "Added coefficients directly (3 + 4 + 5 = 12)",
            "C": "Used 3 + 4 = 7 ignoring constant 5",
            "D": "Gave only the constant term"
        }
    },
    {
        "id": 36,
        "subject": "Mathematics",
        "topic": "Trigonometry",
        "difficulty": "Hard",
        "question": (
            "The value of tan⁻¹(1) + tan⁻¹(2) + tan⁻¹(3) is:"
        ),
        "options": {
            "A": "π",
            "B": "π / 2",
            "C": "3π / 4",
            "D": "0"
        },
        "answer": "A",
        "explanation": (
            "We know tan⁻¹(1) = π/4.\n"
            "For tan⁻¹(2) + tan⁻¹(3): since xy = 2 × 3 = 6 > 1, formula is:\n"
            "tan⁻¹(x) + tan⁻¹(y) = π + tan⁻¹[(x + y) / (1 − xy)].\n"
            "tan⁻¹(2) + tan⁻¹(3) = π + tan⁻¹[(2 + 3) / (1 − 6)] = π + tan⁻¹[5 / (−5)] = π + tan⁻¹(−1) = π − π/4 = 3π/4.\n"
            "Total = tan⁻¹(1) + (3π/4) = π/4 + 3π/4 = π."
        ),
        "distractor_info": {
            "B": "Formula mistake — forgot to add π when xy > 1",
            "C": "Gave only the sum tan⁻¹(2) + tan⁻¹(3)",
            "D": "Sign error"
        }
    },
    {
        "id": 37,
        "subject": "Mathematics",
        "topic": "Trigonometry",
        "difficulty": "Very Hard",
        "question": (
            "The value of the product cos 20° cos 40° cos 60° cos 80° is:"
        ),
        "options": {
            "A": "1 / 16",
            "B": "1 / 8",
            "C": "1 / 32",
            "D": "3 / 16"
        },
        "answer": "A",
        "explanation": (
            "We know cos 60° = 1/2.\n"
            "Product = (1/2) × [cos 20° cos 40° cos 80°].\n"
            "Using identity cos θ cos(60°−θ) cos(60°+θ) = (1/4) cos 3θ:\n"
            "For θ = 20°: cos 20° cos 40° cos 80° = (1/4) cos 60° = (1/4) × (1/2) = 1/8.\n"
            "Therefore, total product = (1/2) × (1/8) = 1 / 16."
        ),
        "distractor_info": {
            "B": "Forgot the cos 60° = 1/2 factor",
            "C": "Extra factor of 1/2 added",
            "D": "Confused with sine product"
        }
    },
    {
        "id": 38,
        "subject": "Mathematics",
        "topic": "Trigonometry",
        "difficulty": "Hard",
        "question": (
            "In a triangle ABC, if a = 3, b = 4, and c = 5, then the value of cos A is:"
        ),
        "options": {
            "A": "4 / 5",
            "B": "3 / 5",
            "C": "0",
            "D": "1 / 2"
        },
        "answer": "A",
        "explanation": (
            "Using Cosine Rule: cos A = (b² + c² − a²) / (2 b c).\n"
            "a = 3, b = 4, c = 5 (this is a right-angled triangle with C = 90°).\n"
            "cos A = (4² + 5² − 3²) / (2 × 4 × 5) = (16 + 25 − 9) / 40 = 32 / 40 = 4 / 5."
        ),
        "distractor_info": {
            "B": "Gave sin A instead of cos A",
            "C": "Confused angle A with right angle C",
            "D": "Used wrong formula"
        }
    },
    {
        "id": 39,
        "subject": "Mathematics",
        "topic": "Trigonometry",
        "difficulty": "Hard",
        "question": (
            "If A + B + C = π in a triangle ABC, then the value of "
            "sin 2A + sin 2B + sin 2C is equal to:"
        ),
        "options": {
            "A": "4 sin A sin B sin C",
            "B": "4 cos A cos B cos C",
            "C": "2 sin A sin B sin C",
            "D": "1 + 4 sin(A/2) sin(B/2) sin(C/2)"
        },
        "answer": "A",
        "explanation": (
            "Standard conditional trigonometric identity for triangle ABC (A + B + C = π):\n"
            "sin 2A + sin 2B = 2 sin(A + B) cos(A − B) = 2 sin(π − C) cos(A − B) = 2 sin C cos(A − B).\n"
            "sin 2C = 2 sin C cos C = 2 sin C cos(π − (A + B)) = −2 sin C cos(A + B).\n"
            "Sum = 2 sin C [cos(A − B) − cos(A + B)] = 2 sin C [2 sin A sin B] = 4 sin A sin B sin C."
        ),
        "distractor_info": {
            "B": "Confused with cos 2A + cos 2B + cos 2C identity",
            "C": "Calculation mistake — missed factor of 2 in product formula",
            "D": "Confused with sin A + sin B + sin C half-angle identity"
        }
    },
    {
        "id": 40,
        "subject": "Mathematics",
        "topic": "Trigonometry",
        "difficulty": "Very Hard",
        "question": (
            "From the top of a tower 100 m high, the angles of depression of two objects on the ground "
            "on the same side of the tower are 45° and 30°. The distance between the two objects is:"
        ),
        "options": {
            "A": "100(√3 − 1) m",
            "B": "100(√3 + 1) m",
            "C": "50(√3 − 1) m",
            "D": "100 / √3 m"
        },
        "answer": "A",
        "explanation": (
            "Let tower height h = 100 m.\n"
            "Distance to first object x₁ = h / tan 45° = 100 / 1 = 100 m.\n"
            "Distance to second object x₂ = h / tan 30° = 100 / (1/√3) = 100√3 m.\n"
            "Distance between objects = x₂ − x₁ = 100√3 − 100 = 100(√3 − 1) m ≈ 100(1.732 − 1) = 73.2 m."
        ),
        "distractor_info": {
            "B": "Calculation mistake — added distances instead of subtracting",
            "C": "Formula mistake — halved tower height",
            "D": "Calculation mistake — omitted first object distance"
        }
    },
    {
        "id": 41,
        "subject": "Mathematics",
        "topic": "Trigonometry",
        "difficulty": "Hard",
        "question": (
            "The number of solutions of the quadratic trigonometric equation "
            "2 sin²x + 3 sin x − 2 = 0 in the interval [0, 2π] is:"
        ),
        "options": {
            "A": "2",
            "B": "4",
            "C": "1",
            "D": "3"
        },
        "answer": "A",
        "explanation": (
            "Factorise: 2 sin²x + 4 sin x − sin x − 2 = 0\n"
            "=> 2 sin x(sin x + 2) − 1(sin x + 2) = 0\n"
            "=> (2 sin x − 1)(sin x + 2) = 0.\n\n"
            "Case 1: sin x = −2 (impossible, since −1 ≤ sin x ≤ 1).\n"
            "Case 2: 2 sin x = 1  =>  sin x = 1/2.\n"
            "In [0, 2π], sin x = 1/2 gives two solutions: x = π/6 and x = 5π/6.\n"
            "Total valid solutions = 2."
        ),
        "distractor_info": {
            "B": "Included invalid solutions from sin x = -2",
            "C": "Found only the first quadrant solution x = π/6",
            "D": "Added extra solution from incorrect interval extension"
        }
    },
    {
        "id": 42,
        "subject": "Mathematics",
        "topic": "Trigonometry",
        "difficulty": "Very Hard",
        "question": (
            "The value of the inverse trigonometric expression "
            "sin⁻¹(sin(2π/3)) + cos⁻¹(cos(7π/6)) + tan⁻¹(tan(3π/4)) is:"
        ),
        "options": {
            "A": "11π / 12",
            "B": "3π / 4",
            "C": "7π / 6",
            "D": "5π / 4"
        },
        "answer": "A",
        "explanation": (
            "Evaluate each term using principal branch values:\n"
            "1. sin⁻¹(sin(2π/3)): sin(2π/3) = sin(π − π/3) = sin(π/3).\n"
            "   Since π/3 ∈ [−π/2, π/2], sin⁻¹(sin(2π/3)) = π/3.\n"
            "2. cos⁻¹(cos(7π/6)): cos(7π/6) = cos(2π − 5π/6) = cos(5π/6).\n"
            "   Since 5π/6 ∈ [0, π], cos⁻¹(cos(7π/6)) = 5π/6.\n"
            "3. tan⁻¹(tan(3π/4)): tan(3π/4) = tan(π − π/4) = −tan(π/4) = tan(−π/4).\n"
            "   Since −π/4 ∈ (−π/2, π/2), tan⁻¹(tan(3π/4)) = −π/4.\n\n"
            "Sum = π/3 + 5π/6 − π/4 = (4π + 10π − 3π) / 12 = 11π / 12."
        ),
        "distractor_info": {
            "B": "Naively removed functions without principal range restriction (2π/3 + 7π/6 + 3π/4)",
            "C": "Sign error on inverse tangent term",
            "D": "Forgot to subtract π/4 for tan term"
        }
    },
    {
        "id": 43,
        "subject": "Mathematics",
        "topic": "Trigonometry",
        "difficulty": "Hard",
        "question": (
            "The exact value of the product sin 10° sin 50° sin 70° is:"
        ),
        "options": {
            "A": "1 / 8",
            "B": "1 / 4",
            "C": "1 / 16",
            "D": "√3 / 8"
        },
        "answer": "A",
        "explanation": (
            "Use the standard trigonometric identity: sin θ sin(60°−θ) sin(60°+θ) = (1/4) sin 3θ.\n"
            "Let θ = 10°:\n"
            "sin 10° sin(60°−10°) sin(60°+10°) = sin 10° sin 50° sin 70°.\n"
            "= (1/4) sin(3 × 10°) = (1/4) sin 30° = (1/4) × (1/2) = 1 / 8."
        ),
        "distractor_info": {
            "B": "Forgot factor of 1/2 from sin 30°",
            "C": "Extra factor of 1/2 added",
            "D": "Confused with cosine product series"
        }
    },
    {
        "id": 44,
        "subject": "Mathematics",
        "topic": "Integrals",
        "difficulty": "Hard",
        "question": (
            "The value of the definite integral ∫₀^(π/2) (√sin x) / (√sin x + √cos x) dx is:"
        ),
        "options": {
            "A": "π / 4",
            "B": "π / 2",
            "C": "π",
            "D": "0"
        },
        "answer": "A",
        "explanation": (
            "Let I = ∫₀^(π/2) (√sin x) / (√sin x + √cos x) dx  --- (1)\n"
            "Use King's Property: ∫₀^a f(x) dx = ∫₀^a f(a − x) dx.\n"
            "I = ∫₀^(π/2) [√sin(π/2 − x)] / [√sin(π/2 − x) + √cos(π/2 − x)] dx\n"
            "I = ∫₀^(π/2) (√cos x) / (√cos x + √sin x) dx  --- (2)\n"
            "Add (1) and (2): 2I = ∫₀^(π/2) (√sin x + √cos x) / (√sin x + √cos x) dx = ∫₀^(π/2) 1 dx = π/2.\n"
            "Therefore, I = π / 4."
        ),
        "distractor_info": {
            "B": "Forgot to divide 2I by 2",
            "C": "Formula mistake — evaluated upper limit directly",
            "D": "Calculation mistake"
        }
    },
    {
        "id": 45,
        "subject": "Mathematics",
        "topic": "Integrals",
        "difficulty": "Hard",
        "question": (
            "The area of the region bounded by the curve y = x² and the line y = x is:"
        ),
        "options": {
            "A": "1 / 6",
            "B": "1 / 3",
            "C": "1 / 2",
            "D": "5 / 6"
        },
        "answer": "A",
        "explanation": (
            "Find points of intersection: x² = x  =>  x(x − 1) = 0  =>  x = 0 and x = 1.\n"
            "In [0, 1], line y = x is above parabola y = x².\n"
            "Area = ∫₀¹ (x − x²) dx = [x²/2 − x³/3]₀¹ = (1/2 − 1/3) − 0 = 1 / 6."
        ),
        "distractor_info": {
            "B": "Calculation mistake — evaluated only ∫₀¹ x² dx = 1/3",
            "C": "Calculation mistake — evaluated only ∫₀¹ x dx = 1/2",
            "D": "Calculation mistake — added areas instead of subtracting"
        }
    }
]


def get_question_bank():
    """Returns the complete 45-question PCM mock test bank."""
    return QUESTIONS
