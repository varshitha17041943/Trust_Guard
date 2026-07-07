from .implementations import (
    WhoisTool, SSLTool, VirusTotalTool, GoogleSafeBrowsingTool, 
    OpenPhishTool, URLHausTool, DNSTool, BrandSimilarityTool, 
    OfficialWebsiteFinderTool, ThreatAggregatorTool, 
    ReportGeneratorTool, EmbeddingGeneratorTool
)

tool_registry = {
    "whois_lookup": WhoisTool(),
    "ssl_checker": SSLTool(),
    "virustotal_lookup": VirusTotalTool(),
    "google_safe_browsing": GoogleSafeBrowsingTool(),
    "openphish_lookup": OpenPhishTool(),
    "urlhaus_lookup": URLHausTool(),
    "dns_lookup": DNSTool(),
    "brand_similarity": BrandSimilarityTool(),
    "official_website_finder": OfficialWebsiteFinderTool(),
    "threat_aggregator": ThreatAggregatorTool(),
    "report_generator": ReportGeneratorTool(),
    "embedding_generator": EmbeddingGeneratorTool(),
}
