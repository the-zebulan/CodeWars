def conference_picker(visited, offered):
    visited = set(visited)
    return next((city for city in offered if city not in visited),
                'No worthwhile conferences this year!')
