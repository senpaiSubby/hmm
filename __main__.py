from hmm import app

if __name__ == "__main__":
    try:
        app.run(debug=True, host="0.0.0.0", port=5000)
    except KeyboardInterrupt:
        pass
