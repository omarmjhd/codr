package net.cloudapp.codr.codrandroid;

import android.support.v7.app.ActionBarActivity;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.view.Window;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;


public class MainActivity extends ActionBarActivity {

    private WebView webView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        /* WEB VIEW ---------------------------------------------------------------------------*/
        // Initialize and attach id
        webView = (WebView) findViewById(R.id.activity_main_webview);
        // Enable JavaScript
        webView.getSettings().setJavaScriptEnabled(true);
        // Load main web page
        webView.loadUrl("http://codr.cloudapp.net");
        // Force links and redirects to open in the app, instead of using an external browser app
        webView.setWebViewClient(new WebViewClient());

    }


    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_main, menu);
        return true;
    }
}
