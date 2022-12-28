import google.colab, gspread, google.auth, os, IPython.display

def eq_backtests(eq_credentials_path: str = 'EQCredentials', *argc, **argv) -> 'EQBacktests':
    # Read EQCredentials
    google.colab.auth.authenticate_user()
    gspread.gc = gspread.authorize(google.auth.default()[0])
    eq_credentials = {
        v[0]:v[1]
        for v in gspread.gc.open(eq_credentials_path).sheet1.get_all_values()[1:]
    }
    
    # Install Library
    os.system(f"pip install git+https://{eq_credentials['GitHub_Username']}:{eq_credentials['GitHub_Token']}@github.com/exp-Quant/EQBacktests@v20")

    # Clean pip install output
    IPython.display.clear_output()

    # Import and return library
    import eq_backtests
    return eq_backtests.EQBacktests(eq_credentials, *argc, **argv)
