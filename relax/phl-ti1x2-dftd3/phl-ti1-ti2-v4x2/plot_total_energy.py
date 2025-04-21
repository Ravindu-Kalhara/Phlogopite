import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def extract_total_energies(file_path):
    energies = []
    with open(file_path, "r") as file:
        for line in file:
            if "!" in line.lower():
                parts = line.split("=")
                if len(parts) > 1:
                    try:
                        energies.append(float(parts[-1].strip().split()[0]))
                    except ValueError:
                        pass
    return energies

# File paths
file_paths = ["relax-prev01.out", "relax.out"]

total_energy_values = [energy for file in file_paths for energy in extract_total_energies(file)]
energy_variations = np.abs(np.diff(total_energy_values))
steps = np.arange(1, len(total_energy_values) + 1)


fig, axs = plt.subplots(1, 2, figsize=(12, 5))

# Total Energy vs Step
axs[0].plot(steps, total_energy_values, marker='o', linestyle='-', color='b', markersize=4, label="Total Energy")
axs[0].set_xlabel("Step")
axs[0].set_ylabel("Total Energy (Ry)")
axs[0].set_title("Total Energy vs Step")
axs[0].grid(True, linestyle="--", alpha=0.6)
axs[0].legend()
axs[0].yaxis.set_major_formatter(ticker.ScalarFormatter(useMathText=True))
axs[0].ticklabel_format(style='sci', axis='y', scilimits=(-2, 2))

# Energy Difference vs Step
axs[1].plot(steps[1:], energy_variations, marker='o', linestyle='-', color='r', markersize=4, label=r"$|E_{n+1} - E_{n}|$")
axs[1].set_xlabel("Step")
axs[1].set_ylabel(r"$|E_{n+1} - E_{n}|$ (Ry)")
axs[1].set_title(r"$|E_{n+1} - E_{n}|$ vs Step")
axs[1].axhline(y=1e-4, color='k', linestyle='--', linewidth=1, label="etot_conv_thr")
axs[1].grid(True, linestyle="--", alpha=0.6)
axs[1].legend()
axs[1].yaxis.set_major_formatter(ticker.ScalarFormatter(useMathText=True))
axs[1].ticklabel_format(style='sci', axis='y', scilimits=(-2, 2))

plt.tight_layout()
plt.show()
