import gifos
import os

# Set GITHUB_TOKEN env var or pass via GitHub Actions secrets

# Fetch GitHub stats
stats = gifos.utils.fetch_github_stats(user_name="DouglasMin")

# Terminal setup
t = gifos.Terminal(width=800, height=500, xpad=15, ypad=15)
t.set_fps(15)

# --- BIOS Boot Screen ---
t.gen_text("GIFOS BIOS v1.0.3", 1, contin=False)
t.gen_text("Copyright (C) 2024, Douglas Min", 2, contin=False)
t.clone_frame(15)

t.gen_text("Memory Test: ", 4, contin=False)
for i in range(0, 640, 64):
    t.gen_text(f"{i}K", 4, col_num=14, contin=False)
    t.clone_frame(2)
t.gen_text("640K OK", 4, col_num=14, contin=False)
t.clone_frame(10)

t.gen_text("Booting from Hard Disk...", 6, contin=False)
t.clone_frame(20)
t.clear_frame()

# --- Login ---
t.gen_text("gifos login: ", 1, contin=False)
t.clone_frame(10)
t.gen_typing_text("douglasmin", 1, contin=True)
t.clone_frame(5)

t.gen_text("Password: ", 2, contin=False)
t.clone_frame(5)
t.gen_typing_text("********", 2, contin=True)
t.clone_frame(10)

t.gen_text("Last login: Welcome back, Douglas!", 3, contin=False)
t.clone_frame(15)
t.clear_frame()

# --- Neofetch Style ---
# ASCII Art (left side)
art = [
    "  \x1b[36m     .--.      \x1b[0m",
    "  \x1b[36m    |o_o |     \x1b[0m",
    "  \x1b[36m    |:_/ |     \x1b[0m",
    "  \x1b[36m   //   \\ \\    \x1b[0m",
    "  \x1b[36m  (|     | )   \x1b[0m",
    "  \x1b[36m /'\\_   _/`\\   \x1b[0m",
    "  \x1b[36m \\___)=(___/   \x1b[0m",
]

info_lines = [
    f"\x1b[36;1mdouglasmin\x1b[0m@\x1b[36;1mgithub\x1b[0m",
    "\x1b[36m---------------------\x1b[0m",
    f"\x1b[36;1mName\x1b[0m:      Douglas Min",
    f"\x1b[36;1mRole\x1b[0m:      Full-Stack Developer",
    f"\x1b[36;1mLocation\x1b[0m:  Seoul, South Korea",
    f"\x1b[36;1mFocus\x1b[0m:     Cloud-Native & GenAI",
    "",
]

# Add live stats if available
if stats:
    info_lines.extend([
        f"\x1b[33;1m--- GitHub Stats ---\x1b[0m",
        f"\x1b[32;1mCommits\x1b[0m:    {stats.total_commits_all_time}",
        f"\x1b[32;1mStars\x1b[0m:      {stats.total_stargazers}",
        f"\x1b[32;1mFollowers\x1b[0m:  {stats.total_followers}",
        f"\x1b[32;1mPRs\x1b[0m:        {stats.total_pull_requests_made} ({stats.total_pull_requests_merged} merged)",
        f"\x1b[32;1mIssues\x1b[0m:     {stats.total_issues}",
        f"\x1b[32;1mContrib To\x1b[0m: {stats.total_repo_contributions} repos",
        f"\x1b[32;1mRank\x1b[0m:       {stats.user_rank.level} (top {stats.user_rank.percentile:.1f}%)",
        "",
    ])

    # Languages
    if stats.languages_sorted:
        info_lines.append(f"\x1b[33;1m--- Languages ---\x1b[0m")
        for lang, pct in stats.languages_sorted[:6]:
            bar_len = int(pct / 5)
            bar = "#" * bar_len + "-" * (20 - bar_len)
            info_lines.append(f"\x1b[35;1m{lang:<12}\x1b[0m [{bar}] {pct:.1f}%")

# Prompt line
t.gen_text("\x1b[36;1mdouglasmin\x1b[0m@\x1b[36;1mgithub\x1b[0m ~> neofetch", 1, contin=False)
t.clone_frame(15)

# Render art + info side by side
for i, art_line in enumerate(art):
    row = i + 3
    t.gen_text(art_line, row, contin=False)

for i, info_line in enumerate(info_lines):
    row = i + 3
    t.gen_text("  " + info_line, row, col_num=20, contin=False)
    t.clone_frame(3)

t.clone_frame(30)

# --- Prompt at bottom ---
last_row = 3 + max(len(art), len(info_lines)) + 1
t.gen_text("\x1b[36;1mdouglasmin\x1b[0m@\x1b[36;1mgithub\x1b[0m ~> ", last_row, contin=False)
t.toggle_blink_cursor(True)
t.clone_frame(30)

# Generate
t.gen_gif()
print("GIF generated: output.gif")
