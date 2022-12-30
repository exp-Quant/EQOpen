import google.colab, gspread, google.auth, subprocess

def eqbacktests(eq_credentials_path: str = 'EQCredentials', *argc, **argv) -> 'EQBacktests':
    # Read EQCredentials
    google.colab.auth.authenticate_user()
    gspread.gc = gspread.authorize(google.auth.default()[0])
    eq_credentials = {
        v[0]:v[1]
        for v in gspread.gc.open(eq_credentials_path).sheet1.get_all_values()[1:]
    }
    
    # Install Library
    subprocess.check_call(['pip', 'install', f"git+https://{eq_credentials['GitHub_Username']}:{eq_credentials['GitHub_Token']}@github.com/exp-Quant/EQBacktests@v20"], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

    # Import and return library
    import eqbacktests
    return eqbacktests.EQBacktests(eq_credentials, *argc, **argv)
