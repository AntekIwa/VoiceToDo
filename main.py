from text_to_speech import Audio
from wake_listener import recognize_speech
from todo import TODO  # zakładam, że ten plik nazywa się `todo_list.py`
audio = Audio()
todo = TODO()

while True:
    audio.speak("Słucham.")
    cmd = recognize_speech()
    print(">> zwrócone cmd:", cmd)
    cmd = cmd.lower().strip(" ?.!")
    if not cmd:
        audio.speak("Nie dosłyszałem.")
        continue
    if "asystent" not in cmd.lower():
        continue

        # -- Dodawanie zadania
    if "dodaj" in cmd.lower():
        task = cmd.lower().split("dodaj")[-1].strip()
        if not task:
            audio.speak("Nie podałeś zadania do dodania.")
            continue
        if todo.add(task):
            audio.task_added(task)
        else:
            audio.task_exist(task)

        # -- Usuwanie zadania po nazwie
    elif "usuń" in cmd.lower() or "skasuj" in cmd.lower() or "wywal" in cmd.lower() :
        task = cmd.lower().split("usuń")[-1].strip()
        if not task:
            audio.speak("Nie podałeś zadania do usunięcia.")
            continue
        if todo.del_task(task):
            audio.task_deleted(task)
        else:
            audio.task_not_found(task)

        # -- Usuwanie zadania po numerze
    elif "usuń numer" in cmd.lower() or "wywal numer" in cmd.lower():
        try:
            idx = int(''.join(filter(str.isdigit, cmd)))
            if todo.del_idx(idx):
                audio.task_deleted(f"numer {idx}")
            else:
                audio.task_index_invalid(idx)
        except ValueError:
            audio.speak("Nie podałeś poprawnego numeru zadania.")

        # -- Czytanie listy zadań
    elif "pokaż" in cmd.lower() or "lista" in cmd.lower() or "co mam zrobić" in cmd.lower():
        audio.read_list(todo.todo)

        # -- Rozmiar listy
    elif "ile zadań" in cmd.lower() or "ile mam" in cmd.lower():
        audio.list_size(len(todo.todo))

        # -- Komenda nieznana
    else:
        audio.speak("Nie rozumiem komendy. Spróbuj ponownie.")
