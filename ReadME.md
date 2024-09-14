Here’s a `README.md` file that explains the purpose and usage of the script:

```markdown
# NFL Player Stats Analyzer and Betting Recommendation Generator

This Python script loads HTML files containing individual NFL player statistics, identifies the player's position, analyzes their statistics, and generates safe betting recommendations along with reasoning. The results are saved as text files named after the respective HTML files.

## Features
- Automatically loads all HTML files from a specified directory.
- Extracts and analyzes NFL player statistics from the HTML files.
- Identifies the player's position based on the HTML file content.
- Suggests safe bets on the player, providing reasoning behind the recommendations.
- Saves the AI-generated response into a text file named after the original HTML file.

## Requirements

- Python 3.8 or later
- The following Python libraries:
  - `langchain`
  - `langchain_community`
  - `FAISS`
  - `OllamaEmbeddings`

To install the required dependencies, run:

```bash
pip install langchain faiss-cpu langchain_community
```

## Usage

1. **Set up your environment:**
   - Clone or download this repository.
   - Install the required libraries by running `pip install` as shown above.

2. **Place HTML files:**
   - Add your HTML files containing NFL player statistics to the `source_directory` (e.g., `path/to/html/files`).

3. **Update script paths:**
   - Modify the script to set the correct paths for your HTML files and the directory where you want to save the output (text files):
     ```python
     source_directory = "path/to/html/files"
     output_directory = "path/to/output/files"
     ```

4. **Run the script:**
   - After placing your HTML files in the specified source directory, run the script:
     ```bash
     python analyze_player_stats.py
     ```

5. **View results:**
   - The AI's analysis and betting recommendations will be saved in text files in the `output_directory`. Each text file will be named after the corresponding HTML file (e.g., `player1.html` -> `player1.txt`).

## Example Output

For an HTML file `player1.html`, the output will be saved in `player1.txt` and might look like:

```
Response for player1.html:

Position: Quarterback
Safe Bet: Player X will likely exceed 250 passing yards in the next game.
Reasoning: Based on the player's recent performance and passing yard trend over the last 3 games...
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
```

### Summary:
This `README.md` explains the purpose of the script, the steps required to set up and run it, and the expected output format. Make sure to adjust paths and commands as needed depending on your specific environment.
