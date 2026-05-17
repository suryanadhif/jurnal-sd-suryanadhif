# Database Schema

## Tabel users

| Field | Type | Keterangan |
|-------|------|------------|
| id | integer | Primary Key |
| username | varchar | Nama pengguna |
| email | varchar | Email pengguna |
| password | varchar | Password terenkripsi |
| avatar_url | text | Foto profil pengguna |

---

## Tabel posts

| Field | Type | Keterangan |
|-------|------|------------|
| id | integer | Primary Key |
| user_id | integer | Foreign Key ke users |
| title | varchar | Judul posting |
| content | text | Isi posting |
| created_at | datetime | Waktu dibuat |