use JSON;
use Data::Dumper;

sub get_data{
    my $url=shift;
    my $object=undef;
    my $page=`GET $url`;
    if($page=~m/<script\s+async\s+type="application\/ld\+json">(.+?)<\/script>/s){
        #my $item=from_json($1);
        my $item=$1;
        if($item=~m/"sku": "(.+?)\s/s){
            $object->{url}=$1;
        }
        if($item=~m/"priceValidUntil":\s+"(.+?)"/s){
            $object->{priceValidUntil}=$1;
        }

        
    }
    return $object;
}


my $url='https://beyeezy.ru/katalog/yeezy-boost-350/adidas-yeezy-boost-350-v2-cmpct-panda/';
my $obj=get_data($url);
print Dumper($obj)