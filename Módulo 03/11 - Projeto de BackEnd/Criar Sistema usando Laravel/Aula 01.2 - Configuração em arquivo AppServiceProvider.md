Edite o arquivo AppServiceProvider.php , que pode ser encontrado no diretório app/Providers e insira o código a seguir nos use e no método boot

<pre class="language-php">
  <code class="language-php">
    namespace App\Providers;

use Illuminate\Support\ServiceProvider;
use Illuminate\Support\Facades\Schema;

class AppServiceProvider extends ServiceProvider
{
    /**
     * Register any application services.
     */
    public function register(): void
    {
        //
    }

    /**
     * Bootstrap any application services.
     */
    public function boot(): void
    {
        Schema::defaultStringLength(191);
    }
}
  </code>
</pre>
