from controllers.api_handler import get_users
from views.dashboard_component import (
    fetch_data_from_api,
    render_dashboard
)

app_state = {
    "items": [],
    "is_loading": True
}

def update_state(new_data):
    app_state["items"] = new_data
    app_state["is_loading"] = False


if __name__ == "__main__":

    # Loading State Minggu 10
    render_dashboard([], True)

    # Integrasi API Minggu 11
    data = fetch_data_from_api(get_users)

    if data:
        update_state(data)

    render_dashboard(
        app_state["items"],
        app_state["is_loading"]
    )