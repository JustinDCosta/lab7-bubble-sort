"""Pygame Bubble Sort visualizer.

Controls:
- Space: pause/resume
- Right arrow: single-step forward (when paused)
- Left arrow: single-step backward (when paused)
- Up arrow: faster playback
- Down arrow: slower playback
- R: restart playback
- Q or Esc or close window: quit
"""

from __future__ import annotations

from cli_inputs import get_numbers_from_user, get_pygame_speed_delay_ms, get_visual_mode
from sorting_logic import SortFrame, build_sort_frames

WINDOW_WIDTH = 1100
WINDOW_HEIGHT = 700
MARGIN_X = 60
BOTTOM_MARGIN = 100
TOP_MARGIN = 120

BACKGROUND = (16, 18, 24)
TEXT = (230, 230, 230)
BAR = (90, 160, 245)
BAR_COMPARE = (245, 196, 80)
BAR_SWAP_LEFT = (78, 214, 119)
BAR_SWAP_RIGHT = (214, 115, 78)
GRID = (45, 50, 65)



def draw_grid(surface, pygame, bar_area_height: int) -> None:
    """Draw subtle horizontal guide lines."""
    for i in range(5):
        y = TOP_MARGIN + int(i * bar_area_height / 4)
        pygame.draw.line(surface, GRID, (MARGIN_X, y), (WINDOW_WIDTH - MARGIN_X, y), 1)


def draw_frame(surface, pygame, font, small_font, frame: SortFrame, mode: str, delay_ms: int) -> None:
    """Render one frame in the Pygame window."""
    surface.fill(BACKGROUND)

    title = font.render("Bubble Sort Visualizer (Pygame)", True, TEXT)
    status = small_font.render(
        f"Mode: {mode} | Event: {frame.event} | Pass: {frame.pass_index} | "
        f"Comparisons: {frame.compare_count} | Swaps: {frame.swap_count} | Delay: {delay_ms} ms",
        True,
        TEXT,
    )
    controls = small_font.render(
        "Controls: Space pause/resume | Left/Right step | Up/Down speed | R restart | Q/Esc quit",
        True,
        TEXT,
    )
    surface.blit(title, (MARGIN_X, 24))
    surface.blit(status, (MARGIN_X, 64))
    surface.blit(controls, (MARGIN_X, 88))

    values = frame.values
    if not values:
        return

    bar_area_width = WINDOW_WIDTH - 2 * MARGIN_X
    bar_area_height = WINDOW_HEIGHT - TOP_MARGIN - BOTTOM_MARGIN
    draw_grid(surface, pygame, bar_area_height)

    count = len(values)
    gap = 6
    bar_width = max(6, (bar_area_width - (count - 1) * gap) // count)

    min_value = min(values)
    max_value = max(values)
    span = max(1, max_value - min_value)

    for i, value in enumerate(values):
        normalized = (value - min_value) / span
        height = max(4, int(normalized * bar_area_height))

        x = MARGIN_X + i * (bar_width + gap)
        y = TOP_MARGIN + (bar_area_height - height)

        color = BAR
        if i == frame.left_idx:
            color = BAR_SWAP_LEFT if frame.event == "swap" else BAR_COMPARE
        elif i == frame.right_idx:
            color = BAR_SWAP_RIGHT if frame.event == "swap" else BAR_COMPARE

        pygame.draw.rect(surface, color, (x, y, bar_width, height), border_radius=3)

        value_label = small_font.render(str(value), True, TEXT)
        label_x = x + (bar_width - value_label.get_width()) // 2
        label_y = max(TOP_MARGIN - 20, y - 24)
        surface.blit(value_label, (label_x, label_y))


def run_visualizer(values: list[int], delay_ms: int, mode: str) -> None:
    """Run the Pygame window and animate generated sort frames."""
    try:
        import pygame
    except ImportError:
        print("Pygame is not installed. Install dependencies with: pip install -r requirements.txt")
        return

    pygame.init()
    pygame.display.set_caption("Bubble Sort Visualizer")
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()

    font = pygame.font.SysFont("consolas", 28)
    small_font = pygame.font.SysFont("consolas", 20)

    frames = build_sort_frames(values, mode)
    frame_index = 0
    paused = False
    elapsed_ms = 0

    running = True
    while running:
        dt = clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                    running = False
                elif event.key == pygame.K_SPACE:
                    paused = not paused
                elif event.key == pygame.K_RIGHT and paused:
                    frame_index = min(frame_index + 1, len(frames) - 1)
                elif event.key == pygame.K_LEFT and paused:
                    frame_index = max(frame_index - 1, 0)
                elif event.key == pygame.K_UP:
                    delay_ms = max(30, int(delay_ms * 0.8))
                elif event.key == pygame.K_DOWN:
                    delay_ms = min(2000, int(delay_ms * 1.25))
                elif event.key == pygame.K_r:
                    frame_index = 0
                    paused = False
                    elapsed_ms = 0

        if not paused and frame_index < len(frames) - 1:
            elapsed_ms += dt
            if elapsed_ms >= delay_ms:
                frame_index += 1
                elapsed_ms = 0

        draw_frame(screen, pygame, font, small_font, frames[frame_index], mode, delay_ms)
        pygame.display.flip()

    pygame.quit()


def main() -> None:
    """Read inputs in terminal, then launch Pygame visualization window."""
    values = get_numbers_from_user(min_count=2)
    delay_ms = get_pygame_speed_delay_ms()
    mode = get_visual_mode()
    run_visualizer(values, delay_ms, mode)


if __name__ == "__main__":
    main()
