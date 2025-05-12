prompt1 = """Analyze the provided photo and extract detailed facial features, including:
Hair color
Nose shape and size
Eye color and shape
Jawline structure
Gender estimation
Forehead size and shape
Presence and description of a moustache (if any)
Estimated age
Lips shape
Identification of moles, dimples, wrinkles, or scars, along with their precise locations.
Provide a concise and organized description for each feature."""
prompt1_feature_list = [
    "Hair color",
    "Nose shape and size",
    "Eye color and shape",
    "Jawline structure",
    "Gender estimation",
    "Forehead size and shape",
    "Presence and description of a moustache (if any)",
    "Estimated age",
    "Lips shape",
    "Identification of moles, dimples, wrinkles, or scars, along with their precise locations"
]



prompt2 = """Analyze the given image and extract the following facial features:
Hair color: Describe the color of the hair.
Hair length: Specify if the hair is short, medium, or long.
Nose shape: Describe the shape of the nose (e.g., round, pointed, wide).
Nose size: Indicate if the nose is small, medium, or large.
Eye color: Identify the color of the eyes.
Eye shape: Describe the shape of the eyes (e.g., almond-shaped, round).
Jawline structure: Describe the structure of the jawline (e.g., sharp, rounded).
Gender: Indicate the perceived gender of the person.
Forehead size: Specify if the forehead is small, medium, or large.
Forehead shape: Describe the shape of the forehead (e.g., round, flat).
Age: Estimate the approximate age of the person in years.
Moustache: Indicate the presence and type of moustache, if any.
Lips shape: Describe the shape of the lips (e.g., thin, full).
Presence of mole: Indicate if a mole is present (True/False).
Presence of dimples: Indicate if dimples are present (True/False).
Presence of wrinkles: Indicate if wrinkles are present (True/False).
Presence of scars: Indicate if scars are present (True/False).
Provide a detailed response for each feature based on the visual characteristics in the image and strictly seperate each feature by a semicolon."""
prompt2_feature_list = [
    "Hair color",
    "Hair length",
    "Nose shape",
    "Nose size",
    "Eye color",
    "Eye shape",
    "Jawline structure",
    "Gender",
    "Forehead size",
    "Forehead shape",
    "Age",
    "Moustache",
    "Lips shape",
    "Presence of mole",
    "Presence of dimples",
    "Presence of wrinkles",
    "Presence of scars"
]


prompt3 = """Extract the following facial features from the image and respond with single-word answers or concise descriptions:

Hair color:
Hair length (short/medium/long):
Nose shape (round/pointed/wide/etc.):
Nose size (small/medium/large):
Eye color:
Eye shape (almond/round/etc.):
Jawline structure (sharp/rounded/etc.):
Gender (male/female/other):
Forehead size (small/medium/large):
Forehead shape (round/flat/etc.):
Age (integer):
Moustache (yes/no):
Lips shape (thin/full/etc.):
Presence of mole (true/false):
Presence of dimples (true/false):
Presence of wrinkles (true/false):
Presence of scars (true/false):
Provide only the single-word or concise answers as requested. Strictly seperate the features by a semicolon."""
prompt3_feature_list = [
    "Hair color",
    "Hair length",
    "Nose shape",
    "Nose size",
    "Eye color",
    "Eye shape",
    "Jawline structure",
    "Gender",
    "Forehead size",
    "Forehead shape",
    "Age",
    "Moustache",
    "Lips shape",
    "Presence of mole",
    "Presence of dimples",
    "Presence of wrinkles",
    "Presence of scars"
]



prompt4 = """From the image, identify and provide a one-word or concise answer for each of the following:
Hair color:
Hair length (short/medium/long):
Nose shape:
Nose size (small/medium/large):
Eye color:
Eye shape:
Jawline structure:
Gender (male/female/other):
Forehead size (small/medium/large):
Forehead shape:
Approximate age (integer):
Moustache (yes/no):
Lips shape:
Mole (true/false):
Dimples (true/false):
Wrinkles (true/false):
Scars (true/false):
Strictly seperate the features by a semicolon"""
prompt4_feature_list = [
    "Hair color",
    "Hair length",
    "Nose shape",
    "Nose size",
    "Eye color",
    "Eye shape",
    "Jawline structure",
    "Gender",
    "Forehead size",
    "Forehead shape",
    "Approximate age",
    "Moustache",
    "Lips shape",
    "Mole",
    "Dimples",
    "Wrinkles",
    "Scars"
]

prompt5 = """Analyze the given image and extract the following facial features and ratios:
Facial Features:
Hair color: Describe the color of the hair.
Hair length: Specify if the hair is short, medium, or long.
Nose shape: Describe the shape of the nose (e.g., round, pointed, wide).
Nose size: Indicate if the nose is small, medium, or large.
Eye color: Identify the color of the eyes.
Eye shape: Describe the shape of the eyes (e.g., almond-shaped, round).
Jawline structure: Describe the structure of the jawline (e.g., sharp, rounded).
Gender: Indicate the perceived gender of the person.
Forehead size: Specify if the forehead is small, medium, or large.
Forehead shape: Describe the shape of the forehead (e.g., round, flat).
Age: Estimate the approximate age of the person in years.
Moustache: Indicate the presence and type of moustache, if any.
Lips shape: Describe the shape of the lips (e.g., thin, full).
Presence of mole: Indicate if a mole is present (True/False).
Presence of dimples: Indicate if dimples are present (True/False).
Presence of wrinkles: Indicate if wrinkles are present (True/False).
Presence of scars: Indicate if scars are present (True/False).
Facial Ratios:
Golden Ratio (Phi): Calculate the ratio of the face’s length to its width.
Vertical Facial Ratios:
Ratio of the height of the forehead to the height of the face.
Ratio of the nose height to the lower face height.
Ratio of the chin height to the lower face height.
Horizontal Facial Ratios:
Ratio of the interocular distance (distance between the eyes) to the width of the face.
Ratio of the nose width to the width of the face.
Ratio of the mouth width to the width of the face.
Proportional Ratios:
Ratio of the eye width to the distance between the eyes.
Ratio of the lip height to the lower face height.
Ratio of the jaw width to the width of the face.
Symmetry Ratios:
Measure the symmetry of the left and right halves of the face.
Provide a detailed response for each feature and ratio based on the visual characteristics in the image. Strictly Separate each feature or ratio with a semicolon."""

prompt5_feature_list = [
    # Facial Features
    "Hair color",
    "Hair length",
    "Nose shape",
    "Nose size",
    "Eye color",
    "Eye shape",
    "Jawline structure",
    "Gender",
    "Forehead size",
    "Forehead shape",
    "Age",
    "Moustache",
    "Lips shape",
    "Presence of mole",
    "Presence of dimples",
    "Presence of wrinkles",
    "Presence of scars",

    # Facial Ratios
    "Golden Ratio (Phi)",

    # Vertical Facial Ratios
    "Height of forehead to height of face ratio",
    "Nose height to lower face height ratio",
    "Chin height to lower face height ratio",

    # Horizontal Facial Ratios
    "Interocular distance to width of face ratio",
    "Nose width to width of face ratio",
    "Mouth width to width of face ratio",

    # Proportional Ratios
    "Eye width to distance between eyes ratio",
    "Lip height to lower face height ratio",
    "Jaw width to width of face ratio",

    # Symmetry Ratios
    "Symmetry of left and right halves of the face"
]

prompt6 = """Analyze the given image and extract the following facial features:
Hair color: Describe the color of the hair;
Nose shape: Describe the shape of the nose (e.g., straight, curved, wide, narrow);
Eye color: Identify the color of the eyes;
Eye shape: Describe the shape of the eyes (e.g., almond-shaped, round, hooded);
Gender: Indicate the perceived gender of the person;
Approximate age range: Estimate the age range in years (e.g., 20–30, 30–40);
Moustache presence: Indicate whether a moustache is present (Yes/No);
Moustache color: If present, describe the color of the moustache;
Presence of wrinkles: Indicate if wrinkles are visible (True/False);
Eyebrow color: Describe the color of the eyebrows;
Lips shape: Describe the shape of the lips (e.g., thin, full, heart-shaped).

Provide a crisp answers in 1 or 2 words for each feature and strictly separate each feature by a semicolon.
"""
prompt6_feature_list = [
    "Hair color",
    "Nose shape",
    "Eye color",
    "Eye shape",
    "Gender",
    "Approximate age range",
    "Moustache presence",
    "Moustache color",
    "Presence of wrinkles",
    "Eyebrow color",
    "Lips shape"
]