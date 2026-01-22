from deepface import DeepFace

result = DeepFace.verify(
    img1_path="person1.jpg",
    img2_path="person2.jpg",
    model_name="Facenet"
)

print("Is same person:", result["verified"])
