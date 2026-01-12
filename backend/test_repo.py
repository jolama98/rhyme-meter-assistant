from repositories.poem_repository import PoemRepository
from models.poem import Poem

# Create repository instance
repo = PoemRepository()

# Create a test poem
test_poem = Poem(
    title="My First Haiku",
    content="Code flows like water\nPython syntax is so clean\nNo semicolons",
    form_type="haiku"
)

# Save to database
saved_poem = repo.create_poem(test_poem)

print("✅ Poem saved!")
print(f"ID: {saved_poem.id}")
print(f"Title: {saved_poem.title}")
print(saved_poem.to_dict())
